import re
import os


filess = os.listdir(r"./frequency")
for file in filess:
    wordyes, wordno = [], []
    with open(r"./frequency/" + file, "r", encoding="utf-8") as f:
        for line in f.readlines():
            if re.search("^[^<>]+$", line) is not None:
                wordno.append(line)
            else:
                wordyes.append(line)
    with open(r"./frequency/" + file[:3] + "yes.txt", "w+", encoding="utf-8") as y:
        y.write("\n".join(wordyes))
    with open(r"./frequency/" + file[:3] + "no.txt", "w+", encoding="utf-8") as n:
        n.write("\n".join(wordno))
filess = os.listdir(r"./frequency")
for file in filess:
    if re.search("yes", file) is not None:
        with open(r"./frequency/" + file, "r", encoding="utf-8") as f:
            printfile = []
            for line in f.readlines():
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
            with open(r"./frequency/" + file[:3] + "10000.txt", "w+", encoding="utf-8") as w:
                w.write("".join(printfile[:10000]))
