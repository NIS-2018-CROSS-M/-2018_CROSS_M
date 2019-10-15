# Serbian transliteration

**Python code**
```
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
```

## Transliteration

**How to use**
```
$ python3 serbian_transliterator.py serbian_table sr_freq.txt > sr_transliterated.txt
```

**Input example**
```
3086982 у
3083916 је
1854467 и
1142731 се
1133315 на
836809 од
720637 године
658023 су
608754 из
575334 насеље
546565 да
484743 становника
454609 за
401795 са
401637 према
```

**Output example**
```
3086982 u
3083916 je
1854467 i
1142731 se
1133315 na
836809 od
720637 godine
658023 su
608754 iz
575334 naselje
546565 da
484743 stanovnika
454609 za
401795 sa
401637 prema
```
