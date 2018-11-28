

# Data preparation

* Download the following Wikipedias (https://dumps.wikimedia.org/backup-index.html):
  * Russian (e.g. [ruwiki-20181101-pages-articles.xml.bz2](https://dumps.wikimedia.org/ruwiki/20181101/ruwiki-20181101-pages-articles.xml.bz2) from [here](https://dumps.wikimedia.org/ruwiki/20181101/)
  * Czech
  * Polish
  * Ukrainian
  * Belarusian
  * Bulgarian 
  * Macedonian 
  * Slovenian
  * Serbian
  * Croatian
  * Silesian

* Don't forget to save the name of the dump (for reproducibility)

* Extract the text using [WikiExtractor](https://github.com/apertium/WikiExtractor)

* Make a frequency list from each Wikipedia

* Download and compile the following Apertium modules:
  * [`apertium-rus`](https://github.com/apertium/apertium-rus)
  * [`apertium-ces`](https://github.com/apertium/apertium-ces)
  * [`apertium-bul`](https://github.com/apertium/apertium-bul)
  * [`apertium-slv`](https://github.com/apertium/apertium-slv)
  * [`apertium-mkd`](https://github.com/apertium/apertium-mkd)
  * [`apertium-pol`](https://github.com/apertium/apertium-pol)
  * [`apertium-ukr`](https://github.com/apertium/apertium-ukr)
  * [`apertium-bel`](https://github.com/apertium/apertium-bel)
  * [`apertium-hbs`](https://github.com/apertium/apertium-hbs)
  * [`apertium-szl`](https://github.com/apertium/apertium-szl)

* Analyse each frequency list with the analyser and select the top 10,000 open-category forms (`<n>`, `<vblex>`, `<adj>`)

Results will look something like:

```
1917781 ^года/год<n><m><nn><sg><gen>/год²<n><m><nn><sg><gen>/год²<n><m><nn><pl><acc>/год²<n><m><nn><pl><nom>$
1460403 ^году/год<n><m><nn><sg><dat>/год<n><m><nn><sg><prp>/год²<n><m><nn><sg><dat>/год²<n><m><nn><sg><prp>$
1050634 ^был/быть<vbser><past><m><sg>/былой<adj><sint><short><m><sg>$
850890 ^для/для<pr>/длить<vblex><impf><tv><pprs><adv>/длить<vblex><impf><iv><pprs><adv>$
668092 ^до/до<pr>/до<n><nt><nn><sg><nom>/до<n><nt><nn><sg><gen>/до<n><nt><nn><sg><dat>/до<n><nt><nn><sg><acc>/до<n><nt><nn><sg><prp>/до
до<n><nt><nn><pl><nom>/до<n><nt><nn><pl><gen>/до<n><nt><nn><pl><dat>/до<n><nt><nn><pl><acc>/до<n><nt><nn><pl><prp>/до<n><nt><nn><
pl><ins>$
640528 ^он/он<prn><pers><p3><m><sg><nom>/он²<n><nt><nn><sg><nom>/он²<n><nt><nn><sg><gen>/он²<n><nt><nn><sg><dat>/он²<n><nt><nn><sg><acc
он²<n><nt><nn><sg><prp>/он²<n><nt><nn><sg><ins>/он²<n><nt><nn><pl><nom>/он²<n><nt><nn><pl><gen>/он²<n><nt><nn><pl><dat>/он²<n><nt><nn><pl><acc>/он²<
он²<n><nt><nn><pl><ins>$
474296 ^были/быть<vbser><past><mfn><pl>/быль<n><f><nn><sg><gen>/быль<n><f><nn><sg><dat>/быль<n><f><nn><sg><prp>/быль<n><f><nn><pl><nom>
быль<n><f><nn><pl><acc>$
472484 ^была/быть<vbser><past><f><sg>/былой<adj><sint><short><f><sg>$
460999 ^было/быть<vbser><past><nt><sg>/былой<adj><sint><cmp>/былой<adj><sint><short><nt><sg>$
434773 ^при/при<pr>/пря<n><f><nn><sg><gen>/пря<n><f><nn><pl><nom>/пря<n><f><nn><pl><acc>/переть<vblex><impf><tv><imp><p2><sg>/переть<vb
lex><impf><iv><imp><p2><sg>$
426795 ^но/но<cnjcoo>/но<n><nt><nn><sg><nom>/но<n><nt><nn><sg><gen>/но<n><nt><nn><sg><dat>/но<n><nt><nn><sg><acc>/но<n><nt><nn><sg><prp
но<n><nt><nn><sg><ins>/но<n><nt><nn><pl><nom>/но<n><nt><nn><pl><gen>/но<n><nt><nn><pl><dat>/но<n><nt><nn><pl><acc>/но<n><nt><nn><pl><prp>/но<n><nt><
nn><pl><ins>$
337712 ^после/посол<n><m><aa><sg><prp>/после<adv>/после<pr>$
337153 ^же/же<part>/же<n><nt><nn><sg><nom>/же<n><nt><nn><sg><gen>/же<n><nt><nn><sg><dat>/же<n><nt><nn><sg><acc>/же<n><nt><nn><sg><prp>/
же<n><nt><nn><pl><nom>/же<n><nt><nn><pl><gen>/же<n><nt><nn><pl><dat>/же<n><nt><nn><pl><acc>/же<n><nt><nn><pl><prp>/же<n><nt><nn
><pl><ins>$
318197 ^под/под<pr>/под<n><m><nn><sg><nom>/под<n><m><nn><sg><acc>$
309677 ^время/время<n><nt><nn><sg><nom>/время<n><nt><nn><sg><acc>$
296390 ^области/область<n><f><nn><sg><gen>/область<n><f><nn><sg><dat>/область<n><f><nn><sg><prp>/область<n><f><nn><pl><nom>/область<n><
f><nn><pl><acc>$
280765 ^человек/человек<n><m><aa><pl><gen>/человек<n><m><aa><sg><nom>$
...
```

* Write a script to convert this data to the following format:

```
rus	года	год	NOUN	Animacy=Inan|Case=Gen|Gender=Masc|Number=Sing
rus	года	год	NOUN	Animacy=Inan|Case=Acc|Gender=Masc|Number=Plur
rus	года	год	NOUN	Animacy=Inan|Case=Nom|Gender=Masc|Number=Plur
rus	году	год	NOUN	Animacy=Inan|Case=Dat|Gender=Masc|Number=Sing
rus	году	год	NOUN	Animacy=Inan|Case=Loc|Gender=Masc|Number=Sing
...
```

To convert the tags you can use a lookup table like:

```
_	_	acc	_	_	Case=Acc
_	_	nom	_	_	Case=Nom
_	n	_	_	NOUN	_	_
_	adj|sint	_	_	ADJ	_	_
_	adj	_	_	ADJ	_	_
_	vblex	_	_	VERB	_	_
_	vbser	_	_	VERB	_	_
```

In general the POS/features of particular forms should follow the POS/features in the UD treebanks.

You should probably discard:

* Non-open category readings (e.g. `после<pr>`, `но<cnjcoo>`)
* Different paradigm identifiers (`¹`, `²`, ...)

You can think about if you want to discard indeclinable readings (e.g. noun readings for "но")


# Regular expressions

Freq.list:

$ uconv -x lower < DUMPNAME | sed 's/[^REGEX]\+/\n/g' | sort -r | uniq -c | sort -nr > FILENAME

REGEX:
* Russian
    * [а-яА-Я]
* Czech
    * ???
* Polish
    * [a-pr-uwy-zA-PR-UWY-ZąćęłńóśźżĄĆĘŁŃÓŚŹŻ]
* Ukrainian
    * ???
* Belarusian
    * [ёа-зй-шы-яЁА-ЗЙ-ШЫІіЎў] - apostrophe
* Bulgarian 
    * ???
* Macedonian 
    * ???
* Slovenian
    * ???
* Serbian
    * ???
* Croatian
    * ???
* Silesian
    * ???
