# Frequency lists

**Pipeline**

```
$ uconv -x lower < DUMPNAME | sed 's/[^REGEX]\+/\n/g' | sort -r | uniq -c | sort -nr > FILENAME
```

Since we lower the words in the texts before tokenising, sorting and counting, we do not consider uppercase letters in our regular expressions. 
 
**Russian**
```
$ uconv -x lower < ruwiki-20181101-pages-articles.txt | sed 's/[^а-яё]\+/\n/g' | sort -r | uniq -c | sort -nr > ru_freq.hist

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

**Czech**
```
$ uconv -x lower < cswiki-20181120-pages-articles-multistream.txt | sed 's/[^a-záčďéěíňóřšťúůýž]\+/\n/g' | sort -r | uniq -c | sort -nr > cs_freq.hist

$ head cs_freq.hist

3870103 
3326181 v
3233979 a
1919556 se
1744502 na
1296633 je
 818770 z
 781687 s
 750808 do
 611968 byl
```

**Polish**
```
uconv -x lower < plwiki-20181101-pages-articles-multistream.txt | sed 's/[^a-pr-uwy-ząćęłńóśźż]\+/\n/g' | sort -r | uniq -c | sort -nr > pl_freq.hist

head pl_freq.hist

11739624 w
9332135 
4672516 i
3585799 na
3496033 z
2596201 do
2352529 się
1658183 roku
1171855 a
1042590 od
```

**Ukrainian**
```
$ uconv -x lower < ukwiki-20181120-pages-articles-multistream.txt | sed "s/[^а-щьюяїієґ']\+/\n/g" | sort -r | uniq -c | sort -nr > uk_freq.hist

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

**Belarusian**
```
$ uconv -x lower < bewiki-20181120-pages-articles-multistream.txt | sed "s/[^ёа-зй-шы-яіў']\+/\n/g" | sort -r | uniq -c | sort -nr > be_freq.hist

$ head be_freq.hist

1152981 
 677607 і
 641942 у
 572173 ў
 410294 з
 368861 на
 161720 да
 126731 года
 112259 па
 102815 годзе
```

**Bulgarian** 
```
$ uconv -x lower < bgwiki-20181120-pages-articles-multistream.txt | sed 's/[^а-ъьюя]\+/\n/g' | sort -r | uniq -c | sort -nr > bg_freq.hist

$ head bg_freq.hist

3219458 на
2158731 
1867058 и
1733141 в
1449104 е
1241037 от
 816977 се
 730813 за
 588790 с
 545806 г
```

**Macedonian**
```
$ uconv -x lower < mkwiki-20181120-pages-articles-multistream.txt | sed 's/[^а-ик-шѓѕјљњќџ]\+/\n/g' | sort -r | uniq -c | sort -nr > mk_freq.hist

$ head mk_freq.hist
1819398 на
1147923 во
1025096 
 929090 и
 701826 од
 643944 се
 472556 е
 394170 со
 388703 за
 288450 да
```

**Slovenian**
* ???
**Serbian**
* ???
**Croatian**
* ???
**Silesian**
* ???
