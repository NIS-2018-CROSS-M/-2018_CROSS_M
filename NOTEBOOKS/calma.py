#%% [markdown]
# ## set up telegram notifications
# 
# не очень понятно, нужно ли это. если нужно -- напишите @oserikov в телеграме, я расскажу, что сделать, чтобы присылались сообщения с качеством модели когда она отработает. 

#%%
telegram_notifications_enabled=False
EXP_DESCRIPTION = "PREDICT ONLY MORPHOLOGICAL ANALYSIS"

#%%
if telegram_notifications_enabled:
    bot_token = input("введите telegram bot token: ")
    chat_id = "292749902" # for @oserikov

#%% [markdown]
# # prepare

#%%
import sys

#%% [markdown]
# #### install prereqs

#%%

# clone openmt-py used in calma and move it into the proper folder
get_ipython().system('git clone https://github.com/OpenNMT/OpenNMT-py.git')
get_ipython().magic('cd OpenNMT-py')
get_ipython().system('git checkout -b stable-version d57fa68e6b0c2041642af40f76e1d5903c80a9b8')
get_ipython().magic('cd ..')
get_ipython().system('mv OpenNMT-py ~')
get_ipython().system('wget -q https://raw.githubusercontent.com/NIS-2018-CROSS-M/calma/tmp-utils/utils/onmt-decoder.py -O ~/OpenNMT-py/onmt/decoders/decoder.py')
get_ipython().system('wget -q https://raw.githubusercontent.com/NIS-2018-CROSS-M/calma/tmp-utils/utils/onmt-opts.py -O ~/OpenNMT-py/onmt/opts.py')

# clone and run a tool installing pytorch 0.4.1 with cuda 9.2 into colab (maybe works on any ubuntu 16)
get_ipython().system('git clone https://gist.github.com/f7b7c7758a46da49f84bc68b47997d69.git colab_cuda_upgrader')
get_ipython().system('bash colab_cuda_upgrader/pytorch041_cuda92_colab.sh')

# install dependencies used in calma project
get_ipython().system('{sys.executable} -m pip install configargparse')

# install the proper version of torchtext
get_ipython().system('git clone https://github.com/pytorch/text.git')
get_ipython().magic('cd text')
get_ipython().system('{sys.executable} -m pip install .')
get_ipython().magic('cd ..')

# receive the calma
get_ipython().system('git clone https://github.com/ftyers/calma.git')
get_ipython().magic('cd calma')
get_ipython().system('git checkout -b latest-known-version d4ce3758d06538933855f734a44630efc8e2b6b2')
get_ipython().magic('cd sharedtaskdata')
get_ipython().system('rm onmt-data/*')
get_ipython().system('rm results/*')

#%% [markdown]
# #### imports

#%%
from collections import defaultdict as dd
from random import shuffle
import re
import urllib

#%% [markdown]
# ## helping functions definitions

#%%
def score_predictions(res_file_fn, gold_file_fn, output_fn, dataEvaluator):   
    
    def readdata(fn):
        data = {otype:dd(set) for otype in dataEvaluator.otypes}
        for line in open(fn):
            line = line.strip('\n')
            if line:
                data = dataEvaluator.update_data(data, line)
        return data
    
    sysdata = readdata(res_file_fn)
    golddata = readdata(gold_file_fn)
    
    output_f = open(output_fn, 'a+', encoding='utf-8')
    for otype in dataEvaluator.otypes:
        tp = 0
        fp = 0
        fn = 0
        for wf in sysdata[otype]:
            tp += len(sysdata[otype][wf] & golddata[otype][wf])
            fp += len(sysdata[otype][wf] - golddata[otype][wf])
            fn += len(golddata[otype][wf] - sysdata[otype][wf])
        recall = tp/(tp+fn)
        precision = tp/(tp+fp)
        fscore = 2 * recall * precision / (recall + precision)
        print("Recall for %s: %.2f" % (otype,recall*100), file = output_f)
        print("Precision for %s: %.2f" % (otype,precision*100), file = output_f)
        print("F1-score for %s: %.2f" % (otype,fscore*100), file = output_f)
        print("", file = output_f)
    
    output_f.close()

def modify_nbest(nbest_src_filename, nbest_tgt_filename, nbestModifyer):
    with open(nbest_src_filename, 'r', encoding='utf-8') as src_f,         open(nbest_tgt_filename, 'w', encoding='utf-8') as tgt_f:

        for line in src_f.readlines():
            line = line.rstrip('\n').rstrip('\r')
            if line.startswith("SENT "):
                line = nbestModifyer.sent_to_baseline_compatible(line)
            elif re.match("^\[[\-\+]?\d+\.\d+\]\s\[", line):
                line = nbestModifyer.hyp_to_baseline_compatible(line)

            print(line, file=tgt_f)

#%%
def initialize_data(train_src, train_tgt, valid_src, valid_tgt, prepared_training_data_prefix):
    prepr_params = f"-train_src {train_src} -train_tgt {train_tgt} -valid_src {valid_src} -valid_tgt {valid_tgt} -save_data {prepared_training_data_prefix}" 
    get_ipython().system('{sys.executable} ~/OpenNMT-py/preprocess.py {prepr_params}')


def train_ml(train_params):
    train_params = " ".join(train_params)
    get_ipython().system('{sys.executable} ~/OpenNMT-py/train.py {train_params}')


def generate_predictions(generation_params, output_filename):
    generation_params = " ".join(generation_params)
    get_ipython().system('{sys.executable} ~/OpenNMT-py/translate.py {generation_params} > {output_filename}')


def choose_best_predictions(nbest_filename, covered_filename, output_filename):
    get_ipython().system('cat {nbest_filename} | grep -v -P "^\\s+" | grep -v -P "^\\+" | {sys.executable} scripts/get-analyses.py 0.8 3 {covered_filename} > {output_filename}')

#%% [markdown]
# #### def data_generation

#%%
# the method called for each non-processed training data row
def get_data_entry(language, wordform, lemma, pos_tag, morphological_analysis):
    lemma = ' '.join(lemma)
    wordform = ' '.join(wordform)
    morphological_analysis = morphological_analysis.split('|')
    return wordform, '%s %s' % (lemma, ' '.join(['+%s' % x for x in [pos_tag] + morphological_analysis  + ["Language=%s" % language]]))


def generate_onmt_data(fn, res_src_fn, res_tgt_fn, DataModifyerClass):
    
    modify_src_line = DataModifyerClass.modify_src_line
    modify_tgt_line = DataModifyerClass.modify_tgt_line
    restore_orig_src_line = DataModifyerClass.restore_src_line
    restore_orig_tgt_line = DataModifyerClass.restore_tgt_line
    
    analyses = dd(set)

    for line in open(fn, encoding='utf-8'):
        line = line.rstrip('\n').rstrip('\r')
        lang, wf, lemma, pos, msd = line.split('\t')
        wf, a = get_data_entry(lang, wf, lemma, pos, msd)
        analyses[wf].add(a)
    
    tmp_src_fn = res_src_fn + "-default"
    tmp_tgt_fn = res_tgt_fn + "-default"
    
    tmp_src = open(tmp_src_fn, 'w')
    tmp_tgt = open(tmp_tgt_fn, 'w')
    res_src = open(res_src_fn, 'w')
    res_tgt = open(res_tgt_fn, 'w')
    
    analyses = list(analyses.items())
    shuffle(analyses)

    for wf, analysis in analyses:
        for a in analysis:
            print(wf, file = tmp_src)
            print(a, file = tmp_tgt)
            print(modify_src_line(wf), file = res_src)
            print(modify_tgt_line(a), file = res_tgt)

#%% [markdown]
# ### def ml()

#%%
def ml(langs, tracks, train_params, prediction_params, dataModifyer, nbestModifyer, dataEvaluator):
    
    def generate_data(orig_data_fn, res_src_fn, res_tgt_fn):
        return generate_onmt_data(orig_data_fn, res_src_fn, res_tgt_fn, dataModifyer)

    def train(train_res_src_fn, train_res_tgt_fn, val_res_src_fn, val_res_tgt_fn, save_model_fn, train_params):
        data_fn = save_model_fn + "-prepared_training_data" #f"onmt-data/{lang}-track{track}"    
        initialize_data(train_res_src_fn, train_res_tgt_fn, val_res_src_fn, val_res_tgt_fn, data_fn)

        train_params.extend([f"-data {data_fn}", f"-save_model {save_model_fn}"])
        train_ml(train_params)
        get_ipython().system('mv {save_model_fn}_step_{train_steps}.pt {save_model_fn}')

    
    def predict(model_filename, input_data_filename, covered_filename, chosen_output_filename):
        output_data_filename = f"{input_data_filename}.out"
        nbest_output_filename = f"{input_data_filename}.nbest.out"
        prediction_params.extend([
            f"-model {model_filename}",
            f"-src {input_data_filename}",
            f"-output {output_data_filename}"
        ])
        generate_predictions(prediction_params, nbest_output_filename)
        nbest_output_modified_filename = nbest_output_filename+"-modified"
        modify_nbest(nbest_output_filename, nbest_output_modified_filename, nbestModifyer)
        choose_best_predictions(nbest_output_modified_filename, covered_filename, chosen_output_filename)

    
    for lang in langs:
        for track in tracks:
            train_covered_filename = f"train/{lang}-track{track}-covered"
            train_uncovered_filename = f"train/{lang}-track{track}-uncovered"
            val_covered_filename = f"dev/{lang}-covered"
            val_uncovered_filename = f"dev/{lang}-uncovered"
            test_covered_filename = f"test/{lang}-covered"
            test_uncovered_filename = f"test/{lang}-uncovered"

            train_res_src_filename = f"onmt-data/{lang}-track{track}-src-train.txt"
            train_res_tgt_filename = f"onmt-data/{lang}-track{track}-tgt-train.txt"

            val_res_src_filename = f"onmt-data/{lang}-track{track}-src-dev.txt"
            val_res_tgt_filename = f"onmt-data/{lang}-track{track}-tgt-dev.txt"

            test_res_src_filename = f"onmt-data/{lang}-track{track}-src-test.txt"
            test_res_tgt_filename = f"onmt-data/{lang}-track{track}-tgt-test.txt"


            generate_data(train_uncovered_filename, train_res_src_filename, train_res_tgt_filename)        
            generate_data(val_uncovered_filename, val_res_src_filename, val_res_tgt_filename)

            model_filename = f"models/{lang}-track{track}.model"
            train(train_res_src_filename, train_res_tgt_filename, val_res_src_filename, val_res_tgt_filename, model_filename, train_params)


            score_log_filename = f"{lang}-{track}-score.log"
            get_ipython().system('echo "" > {score_log_filename}')

            generate_data(test_covered_filename, test_res_src_filename, test_res_tgt_filename)
            test_pred_output_filename = f"results/{lang}-track{track}-test-covered.sys"
            predict(model_filename, test_res_src_filename, test_covered_filename, test_pred_output_filename)
            get_ipython().system('echo "*===QUALITY ON TEST DATA===*" >> {score_log_filename}')
            score_predictions(test_pred_output_filename, test_uncovered_filename, score_log_filename, dataEvaluator)

            val_pred_output_filename = f"results/{lang}-track{track}-dev-covered.sys"
            predict(model_filename, val_res_src_filename, val_covered_filename, val_pred_output_filename)
            get_ipython().system('echo "*===QUALITY ON VAL DATA===*" >> {score_log_filename}')
            score_predictions(val_pred_output_filename, val_uncovered_filename, score_log_filename, dataEvaluator)

            get_ipython().system('cat {score_log_filename}')
            
            if telegram_notifications_enabled:
                telegram_message = "#score\n"+''.join(open(score_log_filename).readlines())+'\n'+EXP_DESCRIPTION

                telegram_message_encoded = urllib.parse.quote(telegram_message)
                get_ipython().system('curl -i -X GET "https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&text={telegram_message_encoded}&parse_mode=markdown"')

#%% [markdown]
# # ML
#%% [markdown]
# ## set ml params

#%%
langs=['ast']
tracks=['1']
data_classes = ['test', 'dev']

train_steps=1000
valid_steps=100
save_checkpoint_steps = valid_steps

train_params = [
    f"-train_steps {train_steps}",
    f"-valid_steps {valid_steps}",
    f"-save_checkpoint_steps {save_checkpoint_steps}",
    f"-world_size 1",
    f"-gpu_ranks 0 1",
    f"-encoder_type brnn"
]

pred_params = [
    f"-replace_unk",
    f"-verbose",
    f"-n_best 8",
    f"-beam 8"
]

#%% [markdown]
# ## Predict only morphological analysis approach
#%% [markdown]
# #### data description
#%% [markdown]
# **source**
# ```
# wf1 wf2 ... wfN
# ```
# 
# **target**
# ```
# +Tag1=Value1 ... +TagN=ValueN
# ```
# 
# **uncovered**
# (tab separated)
# ```
# langCode	wordForm	lemma	POS	Tag1=Value1|...|TagN=ValueN
# ```
# 
# **prediction** raw
# ```
# SENT 1: ['wf1', 'wf2', ..., 'wfN']
# ...
# [-9.2825] ['+Tag1=Value1', ..., '+TagN=ValueN']
# ```
# **prediction** passed to `eval()`
# ```
# ['c', 'c', '+NOUN', '+Tag1=Value1', ..., '+TagN=ValueN', '+Language=lan']
# ```
# 
# prediction then is converted to follow the uncovered file pattern
# ```
# langCode	wordForm	lemma	POS	Tag1=Value1|...|TagN=ValueN
# ```
# 
# 
#%% [markdown]
# #### embeddings
# * character-level input embeddings
# * character-level output embeddings
# * learned
# * initialized with random
#%% [markdown]
# #### data modification

#%%
class TrainDataModifyer:
    def modify_src_line(line):
        return line


    def restore_src_line(line):
        return line


    def modify_tgt_line(line):
        return ' '.join(['+'+tag for tag in line.split('+') if '=' in tag and not tag.startswith("Language=")]).rstrip(' ')


    def restore_tgt_line(line):
        return line


class NBestDataModifyer:
    def sent_to_baseline_compatible(line):
        return line
                       
    def hyp_to_baseline_compatible(line):
        line_splitted = line.split('] [')
        line_splitted[1] = (line_splitted[1].split(']')[0])
        if len(line_splitted) < 2 or line_splitted[1] == "":
            line_splitted[1] = '\'+Tag0=?\''
        return line_splitted[0] + '] [' + ', '.join(['\'c\'','\'c\'', '\'+NOUN\'', line_splitted[1], '\'+Language=lan\'']) + ']'

    
class DataEvaluator:
    otypes =  ["morph analysis"]
    
    def update_data(data, line):
        lan, wf, lemma, pos, msd = line.split('\t')
        
        data["morph analysis"][wf].add(msd)
        
        return data

#%% [markdown]
# #### ml

#%%
ml(langs, tracks, train_params, pred_params, TrainDataModifyer, NBestDataModifyer, DataEvaluator)

#%% [markdown]
# # sandbox

#%%

