import re
import os
import argparse


# Insert this file together with the folder where frequency apertium files, with morphological analysis, are located.
# This program automatically split the frequency files in three lists:
# "no" list - made from words that apertium could not analyze,
# "yes" list - made from words that apertium could analyze,
# "10000" list - made from the 10000 most frequent words, that are part of an open morphological class (adj, vblex, n)


def process_frequency_files(freq_filenames):
    analyzed_lines_filenames, not_analyzed_lines_filenames = [], []
    for filename in freq_filenames:
        words_analyzed_by_apertium, words_not_analyzed_by_apertium = [], []

        try:
            with open(filename, "r", encoding="utf-8") as freq_f:
                for line in freq_f:
                    if "<" not in line and ">" not in line:
                        words_not_analyzed_by_apertium.append(line)
                    else:
                        words_analyzed_by_apertium.append(line)
        except Exception as e:
            print("problem when processing "+filename+" . Error "+str(e)+" . Skip...")
            continue

        analyzed_lines_filename = filename + "-yes"
        analyzed_lines_filenames.append(analyzed_lines_filename)
        with open(analyzed_lines_filename, "w+", encoding="utf-8") as analyzed_lines_file:
            analyzed_lines_file.writelines(words_analyzed_by_apertium)

        not_analyzed_lines_filename = filename + "-no"
        not_analyzed_lines_filenames.append(not_analyzed_lines_filename)
        with open(not_analyzed_lines_filename, "w+", encoding="utf-8") as not_analyzed_lines_file:
            not_analyzed_lines_file.writelines(words_not_analyzed_by_apertium)

    return analyzed_lines_filenames, not_analyzed_lines_filenames


def get_interesting_analyses_from_word_form_analysis_line(line, interesting_classes=("<n>", "<vblex>", "<adj>")):
    line_as_list = line.split("/")
    word_form = line_as_list[0]
    analyses = line_as_list[1:]
    interesting_analyses = []
    for analysis in analyses:
        if any((interesting_class in analysis) for interesting_class in interesting_classes):
            pretty_analysis = re.sub("[⁰¹²³⁴⁵⁶⁷⁸⁹]", "", analysis)
            interesting_analyses.append(pretty_analysis)
    if interesting_analyses:
        if not interesting_analyses[-1].endswith("$\n"):
            # the format of analyses list requires the list to end up with $ sign and a newline
            interesting_analyses.append("$\n")

    return word_form, interesting_analyses


def get_n_highest_freq_lines(analyzed_word_forms_filenames, top_n_number=10000):
    for filename in analyzed_word_forms_filenames:
        with open(filename, "r", encoding="utf-8") as freq_f:
            output_lines = []
            for line in freq_f:
                word_form, interesting_analyses = get_interesting_analyses_from_word_form_analysis_line(line)

                if interesting_analyses:
                    output_lines.append(word_form + "/" + "/".join(interesting_analyses))

            output_filename = filename + "-top" + str(top_n_number)
            with open(output_filename, "w+", encoding="utf-8") as output_file:
                output_file.write("".join(output_lines[:top_n_number]))


def process_files(filenames):
    analyzed_word_forms_filenames = process_frequency_files(filenames)[0]
    get_n_highest_freq_lines(analyzed_word_forms_filenames)


def process_files_in_dir(path_to_dir):
    files_in_dir = os.listdir(path_to_dir)
    process_files([os.path.join(path_to_dir, f_name) for f_name in files_in_dir])


def main():
    parser = argparse.ArgumentParser(
        description="""Extract top 10000 morphologically analyzed word_forms from the frequency \\t apertium-analysis files.
    If no arguments provided will try to process all the files in the current directory""")
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-d', "--directory", metavar='D', nargs=1, help='process all the files in the direcrory D')
    group.add_argument('-f', "--files", metavar='FILES', nargs='+', help='process all the files in the list FILES')
    args = parser.parse_args()

    if args.files:
        process_files(args.files)
    elif args.directory:
        process_files_in_dir(args.directory[0])
    else:
        process_files_in_dir(os.curdir)


main()
