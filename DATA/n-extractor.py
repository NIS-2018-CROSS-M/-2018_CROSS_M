import re
import os


def get_interesting_analyses_from_lexeme_analysis_line(line):
    line_as_list = line.split("/")
    lexeme = line_as_list[0]
    analyses = line_as_list[1:]
    interesting_analyses = []
    for analysis in analyses:
        # selects only nouns readings and discards others, discards also duplicate readings that apertium generates #
        if "<n>" in analysis:
            if analysis not in interesting_analyses:
                pretty_analysis = re.sub("[⁰¹²³⁴⁵⁶⁷⁸⁹]", "", analysis)
                interesting_analyses.append(pretty_analysis)
    if interesting_analyses: 
        if not interesting_analyses[-1].endswith("$\n"): 
            interesting_analyses.append("$\n")

    return lexeme, interesting_analyses


def check_for_indeclensible(lexeme, analysis, language):
    # how many cases in noun readings for every slavic language #
    declensions = {"rus": 12, "ces": 14, "pol": 12, "ukr": 14, "bel": 12, "bul": 6,
                   "mkd": 4, "slv": 18, "sr": 14, "hr": 14, "sil": 12}
    # clean lexeme from numbers and symbols to compare it with analysis readings #
    lexeme = re.sub("[0-9]+ \\^", "", lexeme)
    # if all lexemes are the same in analyses, and they are included for all cases, put word in indeclensible readings #
    if all(lexeme in analyze for analyze in analysis):
        if len(analysis) == declensions[language]:
            return True
        else:
            return False
    else:
        return False


if __name__ == "__main__":
    # put file outside folder with frequency files, change PATH to your folder name #
    for filean in os.listdir(path="./files/"):
        if filean.endswith(".txt"):
            good_readings = []
            indeclensible_readings = []
            with open("./files/" + filean, "r", encoding="utf-8") as f:
                for line in f.readlines():
                    lex, ans = get_interesting_analyses_from_lexeme_analysis_line(line)
                    if len(ans) != 0:
                        if check_for_indeclensible(lex, ans, re.sub("10000.txt", "", filean)) is False:
                            good_readings.append(lex + "/" + "/".join(ans))
                        else:
                            indeclensible_readings.append(lex + "/" + "/".join(ans))
            # be sure to create a folder named "cleaned" inside your folder with frequency files #
            with open("./files/cleaned/" + filean, "w+", encoding="utf-8") as w:
                w.write("".join(good_readings))
            with open("./files/cleaned/" + "indeclensible" + filean, "w+", encoding="utf-8") as w:
                w.write("".join(indeclensible_readings))
