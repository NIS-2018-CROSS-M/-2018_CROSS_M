# Morphological analysis

**Pipeline**

```
$ apertium -d . MODULENAME-morph < FILENAME1 | cut -f2 -d' ' | paste <(cut -f1 -d' ' FILENAME1) - | sed 's/\t/ /g' > FILENAME2
```

**Russian**
```
$ apertium -d . rus-morph < ru_freq.txt | cut -f2 -d' ' | paste <(cut -f1 -d' ' ru_freq.txt) - | sed 's/\t/ /g' > rumorph.txt

$ head -15 rumorph.txt
 
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

```

**Polish**
```

```

**Ukrainian**
```

```

**Belarusian**
```

```

**Bulgarian** 
```

```

**Macedonian**
```

```

**Slovenian**
```

```

**Serbian**
```

```

**Croatian**
```

```

**Silesian**
```

```
