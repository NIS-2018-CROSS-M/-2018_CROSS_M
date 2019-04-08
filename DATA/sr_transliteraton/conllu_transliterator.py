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
            if line.startswith('# sent_id'):
                print(line)
            elif line.startswith('# text'):
                print(line[:9] + transliterate_line(line[9:], trans_dict))
            elif len(line) > 0:
                conll_line = line.split('\t')

                word = conll_line[1]
                word_cap = word[0].isupper()
                word = transliterate_line(word.lower(), trans_dict)
                if word_cap:
                    word = word.capitalize()

                lemma = conll_line[2]
                lemma_cap = lemma[0].isupper()
                lemma = transliterate_line(lemma.lower(), trans_dict)
                if lemma_cap:
                    lemma = lemma.capitalize()

                conll_line[1] = word
                conll_line[2] = lemma

                print('\t'.join(conll_line))
            else:
                print('\n')


    sys.stdout.close()