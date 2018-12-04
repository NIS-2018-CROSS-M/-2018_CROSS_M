# Frequency lists analysis

### Apertium modules

**Module downloading**

```
$ git clone MODULENAMEURL
```

**Module compiling**

```
# in the module directory
$ sudo ./autogen.sh
$ sudo make
```

### Morphological analysis

**Pipeline**

```
$ apertium -d . rus-morph < FILENAME1 | cut -f2 -d' ' | paste <(cut -f1 -d' ' FILENAME1) - | sed 's/\t/ /g' > FILENAME2
```

**Russian**
```

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
