import morfessor
import math
from collections import Counter

# creates frequency lists from conllu files
def data_prepare(datapath):
    with open(datapath, "r", encoding="utf-8") as r:
        filelist = []
        for line in r.readlines():
            newline = line.split("\t")
            filelist.append(newline[1])
        filelist = Counter(filelist)
        with open(datapath + ".corpus", "a+", encoding="utf-8") as w:
            for key, value in filelist.items():
                w.write(str(value) + " " + key + "\n")

# trains model files (normal, log and type based) and saves them in the script folder
def da_trainer(datapath):
    io = morfessor.MorfessorIO()

    train_data = list(io.read_corpus_file(datapath))

    model_types = morfessor.BaselineModel()
    model_logtokens = morfessor.BaselineModel()
    model_tokens = morfessor.BaselineModel()

    model_types.load_data(train_data, count_modifier=lambda x: 1)
    def log_func(x):
        return int(round(math.log(x + 1, 2)))
    model_logtokens.load_data(train_data, count_modifier=log_func)
    model_tokens.load_data(train_data)

    models = [model_types, model_logtokens, model_tokens]

    i = 0
    for model in models:
        model.train_batch()
        io.write_binary_model_file("model" + str(i), model)

        i += 1

# tags a new Conllu file and returns result on screen
def test_data(modelpath, testpath):
    io = morfessor.MorfessorIO()
    model = io.read_binary_model_file(modelpath)
    test_data = list(io.read_corpus_file(testpath))
    words = test_data[1:-1:6]
    for index, word in enumerate(words):
        words[index] = word[1]
    analyses = []
    for word in words:
        print(model.viterbi_segment(word))

if __name__ == "__main__":
    datapath = r"D:\loren\OneDrive - НИУ Высшая школа экономики\Documenti\Program\vardial-shared-task\train\trk-uncovered.txt"
    modelpath = "model0"
    testpath = r"D:\loren\OneDrive - НИУ Высшая школа экономики\Documenti\Program\vardial-shared-task\dev\trk-uncovered"
    data_prepare(datapath)
    da_trainer(datapath + ".corpus")
    test_data(modelpath, testpath)