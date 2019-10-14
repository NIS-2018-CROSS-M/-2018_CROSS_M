import argparse
import sys


def transliterate_line(text, trans_dict):
    transliterated = ''
    for letter in text:
        if letter in trans_dict:
            transliterated += trans_dict[letter]
        else:
            transliterated += letter
    return transliterated



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('table', help='path to transliteration table')
    parser.add_argument('conllu_file', help='path to conllu file')
    parser.add_argument('-o', dest='output', default=None, help='path to output file (if None - output goes to stdout')
    args = parser.parse_args()

    trans_dict = {}

    with open(args.table) as f:
        for line in f.readlines():
            line = line.strip('\n')
            items = line.split('\t')
            trans_dict[items[0]] = items[1]

    if args.output is not None:
        sys.stdout = open(args.output, 'w')


    with open(args.conllu_file) as c:
        for line in c.readlines():
            line = line.strip()
            line_cap = line[0].isupper()
            line = transliterate_line(line.lower(), trans_dict)
            if line_cap:
                line = line.capitalize()
            print(line)


    sys.stdout.close()
