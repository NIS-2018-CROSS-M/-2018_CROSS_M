udtags = {
    # bidirectional tags: fully compatible between UD and Apertium
    '<n>': 'NOUN',
    '<vblex>': 'VERB',
    '<adj>': 'ADJ',
    # <adj><sint> == <adj> == ADJ
    '<sint>': '',
    # <obj> and <subj> dropped
    '<obj>': '',
    '<subj>': '',
    '<f>': 'Gender=Fem',
    '<m>': 'Gender=Masc',
    '<nt>': 'Gender=Neut',
    '<mfn>': 'Gender=Masc,Fem,Neut',
    '<sg>': 'Number=Sing',
    '<pl>': 'Number=Plur',
    '<du>': 'Number=Dual',
    '<ct>': 'Number=Count',
    '<aa>': 'Animacy=Anim',
    '<an>': 'Animacy=Anim,Inan',
    '<nn>': 'Animacy=Inan',
    '<ind>': 'Definite=Ind',
    '<def>': 'Definite=Def',
    '<comp>': 'Degree=Cmp',
    '<sup>': 'Degree=Sup',
    '<pst>': 'Degree=Pos',
    '<nom>': 'Case=Nom',
    '<acc>': 'Case=Acc',
    '<gen>': 'Case=Gen',
    '<dat>': 'Case=Dat',
    '<ins>': 'Case=Ins',
    '<loc>': 'Case=Loc',
    '<prp>': 'Case=Loc',
    '<voc>': 'Case=Voc',
    '<perf>': 'Aspect=Perf',
    '<impf>': 'Aspect=Imp',
    '<imperf>': 'Aspect=Imp',  # Croatian, archaic imperfect aspect form (Lorenzo). выглядит как еще один вариант
    # имперфекта, нашла несколько разметок апертиума, где этот тег был для имперфекта. Также нашла, что в Апертиуме
    # фича imperfect это ‘pii’ и замаппен через UD как  Tense=Past Mood=Ind. Также в UD есть разметка Aspect = Imp.
    # Что выбрать? Алсо, в хорватском imperfect расценивается как архаизм и стилистический маркер (Nastya)
    '<dual>': 'Aspect=Imp,Perf',
    '<pres>': 'Tense=Pres',
    '<past>': 'Tense=Past',
    '<aor>': 'Tense=Aor',
    '<fut>': 'Tense=Fut',
    '<imp>': 'Mood=Imp',
    '<pp><adv>': ('Tense=Past', 'VerbForm=Vadv'),
    '<pprs><adv>': ('Tense=Pres', 'VerbForm=Vadv'),
    '<tgv><pprs>': 'VerbForm=Conv',
    '<tgv>': 'VerbForm=Conv', # in some perfective readings the pprs tag is not included
    '<pp>': ('Tense=Past', 'VerbForm=Part'),
    '<pprs>': ('Tense=Pres', 'VerbForm=Part'),
    '<inf>': 'VerbForm=Inf',
    '<adv>': 'VerbForm=Vadv',
    '<ger>': 'VerbForm=Vnoun',
    '<short>': 'Variant=Short',
    '<pass>': 'Voice=Pass',
    '<pasv>': 'Voice=Pass',
    '<impers>': 'Voice=Pass',
    '<actv>': 'Voice=Act',
    '<p1>': 'Person=1',
    '<p2>': 'Person=2',
    '<p3>': 'Person=3',
    '<neg>': 'Polarity=Neg',
    '<ma>': ('Gender=Masc', 'Animacy=Anim'),
    '<mi>': ('Gender=Masc', 'Animacy=Inan'),
    '<cpd>': 'Gender=Neut|Number=Sing|Polarity=Pos|Variant=Short|VerbForm=Part|Voice=Pass',
    '<sp>': 'Number=Sing,Plur',
    '<indecl>': 'Case=Indecl',
    '<lp>': 'VerbForm=Part',
    '<pii>': 'Tense=Imp', # Bulgarian and Croatian, following UD tagset as per their website
    '<ssup>': 'Degree=Abs',
    '<futI>': 'Tense=Fut', #serbo-croatian, 2 futures (I and II), UD does not distinguish
    #'<adv>+': 'Degree=Sup'

    # unidirectional tags (not present in UD or used differently)
    '<iv>': 'Valency=1',
    '<tv>': 'Valency=2',
    '<ref>': 'Valency=Refl',  # which tagset to follow for this?
    '<emph>': 'VerbType=Emph',  # check consistency with other tagsets
    '<fac>': 'VerbType=Fact',  # don't add this one наверн, эта разметка на типы глагола есть только в Апертиуме
    '<itg>': 'Type=Inter',  # Possible for verbs as well as for adj and adv, check how to tag properly
    '<cmp>': 'Degree=Com',
    '<prx>': 'Definite=Prx',  # Proximal defined article, Macedonian (no UD model)
    '<dst>': 'Definite=Dst',  # Distal defined article, Macedonian (no UD model)
    '<adj><po>': 'ADV',  # Czech, chorvatsky = по-хорватски, it is an "adverbiated adjective"
    '+htjeti': '', # Croatian, всегда ходят такой цепочкой: <inf>+htjeti<vbmod>. Excluding modal as it concurs to form a regular future form. встречается как кластер <inf>+htjeti<vbmod><clt><futI>. Здесь конструкция хотеть+глагол, где клитик отвечает за окончание глагола “хотеть” (htjeti)
    '<vbmod>': '', # Excluding modal as it is a closed class, only in readings like htjeti or moguci (serbian), where it is an adverbial derived form
    '<clt>': '', # clitics, same reason as per '+htjeti', could be used to mark the "reduced" form of FutI in serbo-croatian if we want to mark it (brace vs. brat ce (more common))
    '<nt>+pos<adj>': 'Poss=Yes' # same reason as htjeti, used to build possessive constructions for name (similar to russian мамина комната)

}


with open(r'E:\Lorenzo Tosi\OneDrive - НИУ Высшая школа экономики\Documenti\Program\NIS-FREQ\frequency\hrmorph.txt-yes-top', 'r', encoding='utf8') as f:
    analyses = []
    for line in f:
        analyses.append(line.split()[1].strip('^$'))

    for analysis in analyses:
        for aptag in udtags.keys():
            if aptag == '<n>' or aptag == '<vblex>' or aptag == '<adj>' or aptag == '<adj><po>':
                analysis = analysis.replace(aptag, '\t' + udtags[aptag])
            elif aptag == '<ma>' or aptag == '<mi>' or aptag == '<pp>' or aptag == '<pprs>'\
                    or aptag == '<pp><adv>' or aptag == '<pprs><adv>':
                analysis = analysis.replace(aptag, '|' + udtags[aptag][0] + '|' + udtags[aptag][1] + '|')
            elif aptag == "<adv>" and "+" in analysis:
                analysis = analysis.replace(aptag, "")
            else:
                analysis = analysis.replace(aptag, '|' + udtags[aptag])

        '''
        todo:
        duplicate analyses
        rus: dat? - поворот поворот NOUN Animacy=Inan|Case=Dat|Gender=Masc|Number=Sing
        ces: nej<adv>+ -> Degree=Sup - nej<adv>+vysoký -, ne<adv>+ -> Polarity=Neg
        discard <indecl>
        '''

        surface_form = analysis.split('/')[0]
        # discard duplicates
        glosses = set(analysis.split('/')[1:])

        for gloss in glosses:
            lemma_and_pos = gloss.split('|')[0]
            gloss = '|'.join(sorted(gloss.split('|')[1:])).strip('|')
            # discard duplicated verb forms
            gloss = gloss.replace('VerbForm=Part|VerbForm=Vadv', '|' + 'VerbForm=Vadv')
            # if '<' in gloss:
            print(surface_form, lemma_and_pos, gloss, sep='\t', file=open(r'E:\Lorenzo Tosi\OneDrive - НИУ Высшая школа экономики\Documenti\Program\NIS-FREQ\frequency\testfile.txt', 'a+', encoding='utf8'))

               
# for hr: (croatian)
    # lp = ??
# also .conllu files (in chat)    
    
