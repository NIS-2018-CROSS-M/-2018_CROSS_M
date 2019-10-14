from collections import defaultdict as dd
import xml.etree.ElementTree as ET
import requests

# todo переписать красиво весь файл

def load_biling_dictionary(filename):
    dictionary = dd(set)

    for section in ET.parse(filename).getroot().iter('section'):
        for translation in section.iter('e'):
            if translation[0].tag == 'p':
                if translation[0][1].text is not None:
                    dictionary[translation[0][0].text].add(translation[0][1].text)
    
    return dictionary


def load_biling_dictionaries(langpair_to_filename):
    dictionaries = {}

    for (src_lang, tgt_lang), dict_fn in langpair_to_filename.items():
        if src_lang not in dictionaries.keys():
            dictionaries[src_lang] = {}    
        dictionaries[src_lang][tgt_lang] = load_biling_dictionary(dict_fn)
    
    return dictionaries
        

def init_lang_info():
    trk_langs=["tat", "tur", "bak", "crh", "kaz", "kir"]
    possible_trk_lang_codes = {lang:[lang] for lang in trk_langs}
    possible_trk_lang_codes["tat"].append("tt")
    possible_trk_lang_codes["kir"].append("ky")

    return trk_langs, possible_trk_lang_codes


def download_apertium_dicts(langs, langcodes, target_folder = "."):
    langpairs_to_filenames = {}

    for lang1 in langs:
        for lang2 in langs:
            possible_repo_names = possible_dict_names = []

            for possible_lang_code1 in langcodes[lang1]:
                for possible_lang_code2 in langcodes[lang2]:
                    possible_repo_names.append(f"apertium-{possible_lang_code1}-{possible_lang_code2}")
                    possible_dict_names.append(f"apertium-{possible_lang_code1}-{possible_lang_code2}.{possible_lang_code1}-{possible_lang_code2}.dix")

            for possible_repo_name in possible_repo_names:
                for possible_dict_name in possible_dict_names:
                    dict_url = f"https://raw.githubusercontent.com/apertium/{possible_repo_name}/master/{possible_dict_name}"
                    response = requests.get(dict_url)
                    if response.status_code == 200:
                        res_f_path = f"{target_folder}/{possible_dict_name}"

                        print(f"wget {dict_url} -O {res_f_path}")
                        langpairs_to_filenames[(lang1, lang2)] = res_f_path
    
    return langpairs_to_filenames


def initialize_translations_ids(dictionaries):
    word_idxs = {}

    for src_lang in dictionaries.keys():
        word_idxs[src_lang] = {}
        for tgt_lang in dictionaries[src_lang].keys():
            word_idxs[tgt_lang] = {}

    for src_lang in dictionaries.keys():
        for tgt_lang in dictionaries[src_lang].keys():
            for word, translations in dictionaries[src_lang][tgt_lang].items():
                word_idxs[src_lang][word] = None
                for translation in translations:
                    word_idxs[tgt_lang][translation] = None
    
    return word_idxs


def get_translation_synonims_sets(dictionaries):
    word_idxs = initialize_translations_ids(dictionaries)

    translations_sets = [{}]

    for src_lang in dictionaries.keys():
        for tgt_lang in dictionaries[src_lang].keys():
            for word, translations in dictionaries[src_lang][tgt_lang].items():
                
                new_translations_set = {(src_lang, word)}
                for translation in translations:
                    new_translations_set.add((tgt_lang, translation))
            
                
                if word_idxs[src_lang][word] is not None:
                    new_translations_set.update(translations_sets[word_idxs[src_lang][word]])
                    translations_sets[word_idxs[src_lang][word]] = {(None, None)}
                else:
                    for translation in translations:
                        if word_idxs[tgt_lang][translation] is not None:
                            new_translations_set.update(translations_sets[word_idxs[tgt_lang][translation]])
                            translations_sets[word_idxs[tgt_lang][translation]] = {(None, None)}
                                        
                new_translations_set.difference_update({(None, None)})
                set_idx = len(translations_sets)
                translations_sets.append(new_translations_set)
                word_idxs[src_lang][word] = set_idx
                for translation in translations:
                    word_idxs[tgt_lang][translation] = set_idx
    
    res = []
    bad_entry = False
    for translation_set in translations_sets:
        bad_entry = False
        if translation_set != {(None, None)} and translation_set != {}:
            for entry in translation_set:
                if entry[1] is None:
                    bad_entry = True
                    
            if not bad_entry:
                res.append(translation_set)        
    return res


langs, langcodes = init_lang_info()
# langpairs_to_filenames = download_apertium_dicts(langs, langcodes)
langpairs_to_filenames = {('tat', 'bak'): './apertium-tat-bak.tat-bak.dix', ('tat', 'kir'): './apertium-tt-ky.tt-ky.dix', ('tur', 'tat'): './apertium-tur-tat.tur-tat.dix', ('tur', 'kir'): './apertium-tur-kir.tur-kir.dix', ('crh', 'tur'): './apertium-crh-tur.crh-tur.dix', ('kaz', 'tat'): './apertium-kaz-tat.kaz-tat.dix', ('kaz', 'tur'): './apertium-kaz-tur.kaz-tur.dix', ('kaz', 'kir'): './apertium-kaz-kir.kaz-kir.dix'}

dictionaries = load_biling_dictionaries(langpairs_to_filenames)

for trans_set in get_translation_synonims_sets(dictionaries):
    print("|".join(["\t".join((entry[1], entry[0])) for entry in trans_set]))


