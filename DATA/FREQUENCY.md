# Frequency lists

**Pipeline**

```
$ uconv -x lower < DUMPNAME | sed 's/[^REGEX]\+/\n/g' | sort -r | uniq -c | sort -nr | sed 's/^ //g' > FILENAME
```

Since we lower the words in the texts before tokenising, sorting and counting, we do not consider uppercase letters in our regular expressions. 
 
**Russian**
```
$ uconv -x lower < ruwiki-20181101-pages-articles.txt | sed 's/[^а-яё]\+/\n/g' | sort -r | uniq -c | sort -nr | sed 's/^ //g' > ru_freq.txt

$ head ru_freq.txt

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
$ uconv -x lower < cswiki-20181120-pages-articles-multistream.txt | sed 's/[^a-záčďéěíňóřšťúůýž]\+/\n/g' | sort -r | uniq -c | sort -nr | sed 's/^ //g' > cs_freq.txt

$ head cs_freq.txt

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
$ uconv -x lower < plwiki-20181101-pages-articles-multistream.txt | sed 's/[^a-pr-uwy-ząćęłńóśźż]\+/\n/g' | sort -r | uniq -c | sort -nr | sed 's/^ //g' > pl_freq.txt

$ head pl_freq.txt

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
$ uconv -x lower < ukwiki-20181120-pages-articles-multistream.txt | sed "s/[^а-щьюяїієґ']\+/\n/g" | sort -r | uniq -c | sort -nr | sed 's/^ //g' > uk_freq.txt

$ head uk_freq.txt

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
$ uconv -x lower < bewiki-20181120-pages-articles-multistream.txt | sed "s/[^ёа-зй-шы-яіў']\+/\n/g" | sort -r | uniq -c | sort -nr | sed 's/^ //g' > be_freq.txt

$ head be_freq.txt

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
$ uconv -x lower < bgwiki-20181120-pages-articles-multistream.txt | sed 's/[^а-ъьюя]\+/\n/g' | sort -r | uniq -c | sort -nr | sed 's/^ //g' > bg_freq.txt

$ head bg_freq.txt

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
$ uconv -x lower < mkwiki-20181120-pages-articles-multistream.txt | sed 's/[^а-ик-шѓѕјљњќџ]\+/\n/g' | sort -r | uniq -c | sort -nr | sed 's/^ //g' > mk_freq.txt

$ head mk_freq.txt

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
```
$ uconv -x lower < slwiki-20181120-pages-articles-multistream.txt | sed 's/[^a-pr-vzčšž]\+/\n/g' | sort -r | uniq -c | sort -nr | sed 's/^ //g' > sl_freq.txt

$ head sl_freq.txt

1481864 je
1409861 
984448 v
915362 in
500453 na
398994 so
386201 se
334624 ki
306842 za
227888 leta
```

**Serbian**
```
$ uconv -x lower < srwiki-20181120-pages-articles-multistream.txt | sed 's/[^а-ик-шђјљњћџ]\+/\n/g' | sort -r | uniq -c | sort -nr | sed 's/^ //g' > sr_freq.txt

$ head sr_freq.txt

4214156 
3086982 у
3083916 је
1854467 и
1142731 се
1133315 на
836809 од
720637 године
658023 су
608754 из
```

**Croatian**
```
$ uconv -x lower < hrwiki-20181120-pages-articles-multistream.txt | sed 's/[^a-pr-vzžčćđš]\+/\n/g' | sort -r | uniq -c | sort -nr | sed 's/^ //g' > hr_freq.txt

$ head hr_freq.txt

1787829 
1621809 je
1499808 i
1487943 u
628194 se
607184 na
486203 su
373546 od
353323 za
299524 a
```

**Silesian**
```
$ uconv -x lower < szlwiki-20181120-pages-articles-multistream.txt | sed 's/[^a-pr-uwyzãčćłńŏōõôřśšůžźż]\+/\n/g' | sort -r | uniq -c | sort -nr | sed 's/^ //g' > szl_freq.txt

$ head szl_freq.txt

29118 
21703 we
9241 a
4876 je
4689 na
3546 ze
3017 do
2823 mjasto
2349 śe
2016 uod
```
