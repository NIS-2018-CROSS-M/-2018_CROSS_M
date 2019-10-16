import sys


serbian = {}


with open(sys.argv[1], 'r') as f:
    for line in f.readlines():
        line = line.strip('\n')
        items = line.split('\t')
        key, serbian[key] = items[0], items[1]


with open(sys.argv[2], 'r') as c:
    for line in c.readlines():
        transliterated = ''
        for letter in line:
            if letter in serbian:
                transliterated += serbian[letter]
            else:
                transliterated += letter
        print(transliterated, end='')
