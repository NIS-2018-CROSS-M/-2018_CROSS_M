# Morphological analysis

**Pipeline**

```
$ cut -f2 -d' ' FILENAME1 | apertium -d . MODULENAME-morph | grep -v -P '^\s*$' | sed 's/ /\n/g' | paste <(cut -f1 -d' ' FILENAME1) - | sed 's/\t/ /g' > FILENAME2
```

**Russian**
```
$ cut -f2 -d' ' ru_freq.txt | apertium -d . rus-morph | grep -v -P '^\s*$' | sed 's/ /\n/g' | paste <(cut -f1 -d' ' ru_freq.txt) - | sed 's/\t/ /g' > rusmorph.txt

$ head -15 rusmorph.txt
 
21097036 ^в/в<pr>$
11915014 ^и/и<cnjcoo>/и<adv>/и²<n><nt><nn><sg><nom>/и²<n><nt><nn><sg><gen>/и²<n><nt><nn><sg><dat>/и²<n><nt><nn><sg><acc>/и²<n><nt><nn><sg><prp>/и²<n><nt><nn><sg><ins>/и²<n><nt><nn><pl><nom>/и²<n><nt><nn><pl><gen>/и²<n><nt><nn><pl><dat>/и²<n><nt><nn><pl><acc>/и²<n><nt><nn><pl><prp>/и²<n><nt><nn><pl><ins>$
6226232 ^на/на<pr>$
4915115 ^с/с<pr>$
3302189 ^года/год<n><m><nn><sg><gen>/год²<n><m><nn><sg><gen>/год²<n><m><nn><pl><acc>/год²<n><m><nn><pl><nom>$
3024134 ^по/по<pr>$
2513118 ^году/год<n><m><nn><sg><dat>/год<n><m><nn><sg><prp>/год²<n><m><nn><sg><dat>/год²<n><m><nn><sg><prp>$
2225703 ^из/из<pr>$
1824770 ^к/к<pr>$
1785046 ^был/быть<vbser><past><m><sg>/былой<adj><sint><short><m><sg>$
1759036 ^не/не<adv>$
1720397 ^а/а<cnjcoo>/а²<n><nt><nn><sg><nom>/а²<n><nt><nn><sg><gen>/а²<n><nt><nn><sg><dat>/а²<n><nt><nn><sg><acc>/а²<n><nt><nn><sg><prp>/а²<n><nt><nn><sg><ins>/а²<n><nt><nn><pl><nom>/а²<n><nt><nn><pl><gen>/а²<n><nt><nn><pl><dat>/а²<n><nt><nn><pl><acc>/а²<n><nt><nn><pl><prp>/а²<n><nt><nn><pl><ins>$
1536360 ^от/от<pr>$
1512058 ^что/что<cnjsub>/что<prn><itg><nt><sg><nom>/что<prn><itg><nt><sg><acc>$
1429097 ^для/для<pr>/длить<vblex><impf><tv><pprs><adv>/длить<vblex><impf><iv><pprs><adv>$
```

**Czech**
```
$ cut -f2 -d' ' cs_freq.txt | apertium -d . ces-morph | grep -v -P '^\s*$' | sed 's/ /\n/g' | paste <(cut -f1 -d' ' cs_freq.txt) - | sed 's/\t/ /g' > cesmorph.txt

$ head -15 cesmorph.txt

3326181 ^v/v<pr>$
3233979 ^a/a<cnjcoo>$
1919556 ^se/se<prn><ref><acc>$
1744502 ^na/na<pr>$
1296633 ^je/být<vbser><pres><p3><sg>/prpers<prn><p3><mf><pl><acc>$
818770 ^z/z<pr>$
781687 ^s/s<pr>$
750808 ^do/do<pr>$
611968 ^byl/být<vbser><past><m><sg>$
606219 ^ve/v<pr>$
566709 ^roce/rok<n><mi><sg><loc>$
502371 ^i/i<cnjcoo>$
483610 ^roku/rok<n><mi><sg><loc>/rok<n><mi><sg><voc>/rok<n><mi><sg><dat>/rok<n><mi><sg><gen>$
476164 ^jako/jako<pr>$
459957 ^o/o<pr>$
```

**Polish**
```
$ cut -f2 -d' ' pl_freq.txt | apertium -d . pol-morph | grep -v -P '^\s*$' | sed 's/ /\n/g' | paste <(cut -f1 -d' ' pl_freq.txt) - | sed 's/\t/ /g' > polmorph.txt

$ head -15 polmorph.txt

11739624 ^w/w<pr>$
4672516 ^i/i<cnjcoo>$
3585799 ^na/na<pr>$
3496033 ^z/z<pr>$
2596201 ^do/do<pr>$
2352529 ^się/się<prn><ref><acc>$
1658183 ^roku/rok<n><mi><sg><gen>/rok<n><mi><sg><loc>/rok<n><mi><sg><voc>$
1171855 ^a/a<cnjcoo>$
1042590 ^od/od<pr>/oda<n><f><pl><gen>$
1040902 ^jest/być<vbser><pres><p3><sg>$
945797 ^przez/przez<pr>$
858765 ^po/po<pr>$
775474 ^oraz/oraz<cnjcoo>$
753969 ^o/o<pr>$
658076 ^został/zostać<vblex><perf><past><p3><m><sg>$
```

**Ukrainian**
```
$ cut -f2 -d' ' uk_freq.txt | apertium -d . ukr-morph | grep -v -P '^\s*$' | sed 's/ /\n/g' | paste <(cut -f1 -d' ' uk_freq.txt) - | sed 's/\t/ /g' > ukrmorph.txt

$ head ukrmorph.txt

3775930 ^в/у<pr><gen>/у<pr><acc>/у<pr><loc>$
3577218 ^у/у<pr><gen>/у<pr><acc>/у<pr><loc>$
3012257 ^на/на<pr><acc>/на<pr><loc>$
2785086 ^і/і<cnjcoo>$
2511419 ^з/з<pr><gen>/з<pr><ins>$
1714686 ^та/та<cnjcoo>/той<prn><dem><f><an><sg><nom>/той<prn><dem><f><an><sg><voc>/той<det><dem><f><an><sg><nom>/той<det><dem><f><an><sg><voc>$
1527968 ^до/до<pr><gen>$
1228118 ^року/рок<n><m><nn><sg><gen>/рок<n><m><nn><sg><dat>/рок<n><m><nn><sg><loc>/рок<n><m><nn><sg><voc>/рік<n><m><nn><sg><gen>/рік<n><m><nn><sg><dat>/рік<n><m><nn><sg><voc>$
1088126 ^за/за<pr>$
1036825 ^що/що<cnjsub><nt><sg><nom>/що<cnjsub><nt><sg><acc>/що<prn><itg><nt><sg><nom>/що<prn><itg><nt><sg><acc>$
811194 ^від/від<pr>$
666104 ^а/а<cnjcoo>$
643888 ^не/не<adv><neg>$
628755 ^для/для<pr>$
611416 ^році/рік<n><m><nn><sg><loc>$
```

**Belarusian**
```
cut -f2 -d' ' be_freq.txt | apertium -d . bel-morph | grep -v -P '^\s*$' | sed 's/ /\n/g' | paste <(cut -f1 -d' ' be_freq.txt) - | sed 's/\t/ /g' > belmorph.txt

$ head -15 belmorph.txt

677607 ^і/і<cnjcoo>$
641942 ^у/у<pr>$
572173 ^ў/у<pr>$
410294 ^з/з<pr>$
368861 ^на/на<pr>$
161720 ^да/да<pr>$
126731 ^года/год<n><m><nn><sg><gen>$
112259 ^па/па<pr>$
102815 ^годзе/годзе<adv>/год<n><m><nn><sg><loc>$
98036 ^ад/ад<pr>$
90178 ^за/за<pr>$
88011 ^а/а<cnjcoo>$
87759 ^быў/быць<vblex><impf><past><m><sg>$
84498 ^не/не<ij>$
82528 ^г/*г$
```

**Bulgarian** 
```
$ cut -f2 -d' ' bg_freq.txt | apertium -d . bul-morph | grep -v -P '^\s*$' | sed 's/ /\n/g' | paste <(cut -f1 -d' ' bg_freq.txt) - | sed 's/\t/ /g' > bulmorph.txt

$ head -15 bulmorph.txt

3227058 ^на/на<pr>$
1869036 ^и/и<cnjcoo>$
1737234 ^в/в<pr>$
1451933 ^е/е<vbser><pres><p3><sg>$
1243709 ^от/от<pr>$
818790 ^се/clitic<prn><ref><pers><mfn><sp><acc>$
732678 ^за/за<pr>$
589953 ^с/с<pr>$
547667 ^г/*г$
511271 ^през/през<pr>$
470827 ^да/да<part>/да<ij>$
436334 ^по/по<pr>$
342690 ^са/е<vbser><pres><p3><pl>$
322438 ^като/като<pr>/като<cnjsub>/като<adv>$
243096 ^си/е<vbser><pres><p2><sg>/clitic<prn><ref><pos>/clitic<prn><ref><pers><mfn><sp><dat>$
```

**Macedonian**
```
$ cut -f2 -d' ' mk_freq.txt | apertium -d . mkd-morph | grep -v -P '^\s*$' | sed 's/ /\n/g' | paste <(cut -f1 -d' ' mk_freq.txt) - | sed 's/\t/ /g' > mkdmorph.txt

$ head -15 mkdmorph.txt

1819398 ^на/на<pr>$
1147923 ^во/во<pr>$
929090 ^и/и<cnjcoo>/clitic<prn><pos><clt><p3><f><sg>/clitic<prn><pers><clt><p3><f><sg><dat>$
701826 ^од/од<pr>$
643944 ^се/е<vbser><pres><p3><mf><pl>/clitic<prn><ref><pers><mfn><sp><acc>$
472556 ^е/е<vbser><pres><p3><mf><sg>$
394170 ^со/со<pr>$
388703 ^за/за<pr>$
288450 ^да/да<ij>/да<part>$
258352 ^година/година<n><f><sg><nom><ind>$
201704 ^како/како<adv>/како<pr>/како<prn><itg>/како<prn><rel>$
178294 ^го/clitic<prn><pers><clt><p3><m><sg><acc>/clitic<prn><pers><clt><p3><nt><sg><acc>$
125543 ^што/што<cnjsub>/што<prn><itg>/што<prn><rel>$
119110 ^а/а<cnjcoo>$
118321 ^ја/clitic<prn><pers><clt><p3><f><sg><acc>$
```

**Slovenian**
```
$ cut -f2 -d' ' sl_freq.txt | apertium -d . slv-morph | grep -v -P '^\s*$' | sed 's/ /\n/g' | paste <(cut -f1 -d' ' sl_freq.txt) - | sed 's/\t/ /g' > slvmorph.txt

$ head -15 slvmorph.txt

1481864 ^je/biti<vbser><pres><p3><sg>/prpers<prn><emph><p3><f><sg><gen>/prpers<prn><emph><p3><f><sg><acc>$
984448 ^v/v<num>/v<pr>$
915362 ^in/in<cnjcoo>$
500453 ^na/na<pr>$
398994 ^so/biti<vbser><pres><p3><pl>$
386201 ^se/se<prn><ref><mf><sp><gen>/se<prn><ref><mf><sp><acc>/se<prn><ref><mf><sp><loc>/se<prn><ref><mf><sp><ins>$
334624 ^ki/ki<cnjsub>$
306842 ^za/za<pr>$
227888 ^leta/let<n><mi><sg><gen>/let<n><mi><du><nom>/let<n><mi><du><acc>/leto<n><nt><sg><gen>/leto<n><nt><pl><nom>/leto<n><nt><pl><acc>/letati<vblex><imperf><pres><p3><sg>$
225323 ^z/z<pr>$
200719 ^s/s<pr>$
200483 ^pa/pa<part>/pa<cnjcoo>$
177506 ^tudi/tudi<part>$
176341 ^da/da<part>/da<cnjsub>/dati<vblex><perf><pres><p3><sg>$
170400 ^kot/kot<cnjsub>/kot<n><mi><sg><nom>/kot<n><mi><sg><acc>/kota<n><f><du><gen>/kota<n><f><pl><gen>$
```

**Serbian**
```

```

**Croatian**
```
$ cut -f2 -d' ' hr_freq.txt | apertium -d . hbs-morph | grep -v -P '^\s*$' | sed 's/ /\n/g' | paste <(cut -f1 -d' ' hr_freq.txt) - | sed 's/\t/ /g' > hrmorph.txt

$ head -15 hrmorph.txt

1621809 ^je/on<prn><pers><clt><p3><f><sg><gen>/on<prn><pers><clt><p3><f><sg><acc>/biti<vbser><clt><pres><p3><sg>$
1499808 ^i/i<cnjcoo>/i<ij>/i<num>/i<part><mod>$
1487943 ^u/u<pr><gen>/u<pr><acc>/u<pr><loc>$
628194 ^se/sebe<prn><ref><clt><pers><mfn><sp><acc>$
607184 ^na/na<pr><acc>/na<pr><loc>$
486203 ^su/biti<vbser><clt><pres><p3><pl>$
373546 ^od/od<pr><gen>$
353323 ^za/za<pr><gen>/za<pr><acc>/za<pr><ins>$
299524 ^a/a<cnjcoo>$
298636 ^s/sa<pr><gen>/sa<pr><ins>$
237932 ^godine/godina<n><f><sg><gen>/godina<n><f><pl><nom>/godina<n><f><pl><acc>/godina<n><f><pl><voc>$
236360 ^da/da<cnjsub>/da<part>/dati<vblex><perf><ref><pres><p3><sg>$
193860 ^kao/kao<cnjsub>/kao<adv>$
184346 ^koji/koji<prn><itg><ma><sg><nom>/koji<prn><itg><ma><pl><nom>/koji<prn><itg><mi><sg><nom>/koji<prn><itg><mi><sg><acc>/koji<prn><itg><mi><pl><nom>/koji<prn><rel><ma><sg><nom>/koji<prn><rel><ma><sg><voc>/koji<prn><rel><ma><pl><nom>/koji<prn><rel><ma><pl><voc>/koji<prn><rel><mi><sg><nom>/koji<prn><rel><mi><sg><acc>/koji<prn><rel><mi><sg><voc>/koji<prn><rel><mi><pl><nom>/koji<prn><rel><mi><pl><voc>$
183393 ^iz/iz<pr><gen>$
```

**Silesian**
```
$ cut -f2 -d' ' szl_freq.txt | apertium -d . szl-morph | grep -v -P '^\s*$' | sed 's/ /\n/g' | paste <(cut -f1 -d' ' szl_freq.txt) - | sed 's/\t/ /g' > szlmorph.txt

$ head -15 szlmorph.txt

21703 ^we/w<pr>$
9241 ^a/a<cnjcoo>$
4876 ^je/być<vbser><pres><p3><sg>$
4689 ^na/na<pr>$
3546 ^ze/ze<pr>$
3017 ^do/do<pr>$
2823 ^mjasto/*mjasto$
2349 ^śe/*śe$
2016 ^uod/*uod$
1991 ^roku/rok<n><mi><sg><gen>/rok<n><mi><sg><loc>/rok<n><mi><sg><voc>$
1945 ^mo/*mo$
1907 ^to/to<det><dem><nt><sg><nom>/to<det><dem><nt><sg><acc>$
1780 ^s/s<n><f><sp><indecl>$
1759 ^sam/sam<adv>$
1532 ^ludźi/*ludźi$
```
