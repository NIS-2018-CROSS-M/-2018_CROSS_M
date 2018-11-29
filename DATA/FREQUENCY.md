# Frequency lists

**Pipeline**

```
$ uconv -x lower < DUMPNAME | sed 's/[^REGEX]\+/\n/g' | sort -r | uniq -c | sort -nr > FILENAME
```


**Russian**
```
$ uconv -x lower < ruwiki-20181101-pages-articles.txt | sed 's/[^а-яёА-ЯЁ]\+/\n/g' | sort -r | uniq -c | sort -nr > ru_freq.hist

$ head ru_freq.hist

21097036 в
17515267 
11915014 и
6226232 на
4915115 с
3302189 года
3024134 по
2513118 году
2225703 из
1824770 к
```

* Czech
* ???
* Polish
```
[a-pr-uwy-zA-PR-UWY-ZąćęłńóśźżĄĆĘŁŃÓŚŹŻ]
```
**Ukrainian**
```
$ uconv -x lower < ukwiki-20181120-pages-articles-multistream.txt | sed "s/[^а-щА-ЩЬьЮюЯяЇїІіЄєҐґ']\+/\n/g" | sort -r | uniq -c | sort -nr > uk_freq.hist

$ head uk_freq.hist

8627722 
3775930 в
3577218 у
3012257 на
2785086 і
2511419 з
1714686 та
1527968 до
1228118 року
1088126 за
```
* Belarusian
```
[ёа-зй-шы-яЁА-ЗЙ-ШЫІіЎў] - apostrophe needed*
```
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
