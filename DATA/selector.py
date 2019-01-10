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


def process_frequency_files(freq_filenames):
    analyzed_lines_filenames, not_analyzed_lines_filenames = [], []
    for filename in freq_filenames:
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
            analyzed_lines_filenames.append(analyzed_lines_filename)

            not_analyzed_lines_filename = output_filename_prefix + "no.txt"
            not_analyzed_lines_filenames.append(not_analyzed_lines_filename)

            with open(r"./frequency/" + analyzed_lines_filename, "w+", encoding="utf-8") as analyzed_lines_file:
                analyzed_lines_file.writelines(words_analyzed_by_apertium)
            with open(r"./frequency/" + not_analyzed_lines_filename, "w+", encoding="utf-8") as not_analyzed_lines_file:
                not_analyzed_lines_file.writelines(words_not_analyzed_by_apertium)

    return analyzed_lines_filenames, not_analyzed_lines_filenames


def get_n_highest_freq_lines(analyzed_lines_filenames):
    for filename in analyzed_lines_filenames:
        with open(r"./frequency/" + filename, "r", encoding="utf-8") as freq_f:
            output_lines = []
            for line in freq_f.readlines():
                line_as_list = line.split("/")

                lexeme = line_as_list[0]
                analyses = line_as_list[1:]
                interesting_analyses = []

                for analysis in analyses:
                    if "<n>" in analysis or "<vblex>" in analysis or "<adj>" in analysis:
                        interesting_analyses.append(analysis)

                if interesting_analyses:
                    if not interesting_analyses[-1].endswith("$\n"):
                        interesting_analyses.append("$\n")

                    output_lines.append(lexeme + "/" + "/".join(interesting_analyses))

            output_filename = get_lang_code_from_freq_file_name(filename) + "10000.txt"

            for index, string in enumerate(output_lines):
                output_lines[index] = re.sub("[⁰¹²³⁴⁵⁶⁷⁸⁹]", "", string)
            with open(r"./frequency/" + output_filename, "w+", encoding="utf-8") as output_file:
                
                output_file.write("".join(output_lines[:10000]))


get_n_highest_freq_lines(process_frequency_files(os.listdir(r"./frequency"))[0])
