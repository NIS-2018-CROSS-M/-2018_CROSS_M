import re
import os

# WIP todo: refactoring !!!
# Insert this file together with the folder where frequency apertium files, with morphological analysis, are located.
# This program automatically split the frequency files in three lists:
# "no" list - made from words that apertium could not analyze,
# "yes" list - made from words that apertium could analyze,
# "10000" list - made from the 10000 most frequent words, that are part of an open morphological class (adj, vblex, n)


# todo: fix silesian lang_code bug
def get_lang_code_from_freq_file_name(filename):
    return filename[:3]


def process_frequency_files(freq_files_names):
    analyzed_lines_files_names, not_analyzed_lines_files_names = [], []
    for filename in freq_files_names:
        if "morph" in filename:
            words_analyzed_by_apertium, words_not_analyzed_by_apertium = [], []

            with open(r"./frequency/" + filename, "r", encoding="utf-8") as freq_f:
                for line in freq_f.readlines():
                    if "<" not in line and ">" not in line:
                        words_not_analyzed_by_apertium.append(line)
                    else:
                        words_analyzed_by_apertium.append(line)

            output_filename_prefix = get_lang_code_from_freq_file_name(filename)

            analyzed_lines_filename = output_filename_prefix + "yes.txt"
            analyzed_lines_files_names.append(analyzed_lines_filename)

            not_analyzed_lines_filename = output_filename_prefix + "no.txt"
            not_analyzed_lines_files_names.append(not_analyzed_lines_filename)

            with open(r"./frequency/" + analyzed_lines_filename, "w+", encoding="utf-8") as analyzed_lines_file:
                analyzed_lines_file.writelines(words_analyzed_by_apertium)
            with open(r"./frequency/" + not_analyzed_lines_filename, "w+", encoding="utf-8") as not_analyzed_lines_file:
                not_analyzed_lines_file.writelines(words_not_analyzed_by_apertium)

    return analyzed_lines_files_names, not_analyzed_lines_files_names


def get_n_highest_freq_lines(analyzed_lines_files_names):
    for filename in analyzed_lines_files_names:
        with open(r"./frequency/" + filename, "r", encoding="utf-8") as freq_f:
            printfile = []
            for line in freq_f.readlines():
                newfile = []
                aa = line.split("/")
                newfile.append(aa[0])
                for index, token in enumerate(aa):
                    if token.find("<n>") is not -1 or token.find("<vblex>") is not -1 or token.find("<adj>") is not -1:
                        newfile.append(token)
                if len(newfile) > 1:
                    if re.search("\$\\n", newfile[-1]) is None:
                        newfile.append("$\n")
                    printfile.append("/".join(newfile))
            with open(r"./frequency/" + filename[:3] + "10000.txt", "w+", encoding="utf-8") as w:
                for index, string in enumerate(printfile):
                    printfile[index] = re.sub("[⁰¹²³⁴⁵⁶⁷⁸⁹]", "", string)
                w.write("".join(printfile[:10000]))


get_n_highest_freq_lines(process_frequency_files(os.listdir(r"./frequency"))[0])
