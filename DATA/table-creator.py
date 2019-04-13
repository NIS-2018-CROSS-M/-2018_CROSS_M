import os
import re
import argparse


udtags = {

    '<n>': 'NOUN',
    '<vblex>': 'VERB',
    '<adj>': 'ADJ',
    # <adj><sint> == <adj> == ADJ
    '<sint>': '',
    # <obj> and <subj> dropped
    '<obj>': '',
    '<subj': '',
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
    '<dual>': 'Aspect=Imp,Perf',
    '<pres>': 'Tense=Pres',
    '<past>': 'Tense=Past',
    '<aor>': 'Tense=Aor',
    '<fut>': 'Tense=Fut',
    '<imp>': 'Mood=Imp',
    '<pp><adv>': ('Tense=Past', 'VerbForm=Vadv'),
    '<pprs><adv>': ('Tense=Pres', 'VerbForm=Vadv'),
    '<tgv><pprs>': 'VerbForm=Trans',  # VerbForm=Conv as per UD V2 guidelines? Form is Transgressive Participle
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
    '<iv>': 'Valency=1',
    '<tv>': 'Valency=2',
    '<neg>': 'Polarity=Neg',
    '<ma>': ('Gender=Masc', 'Animacy=Anim'),
    '<mi>': ('Gender=Masc', 'Animacy=Inan'),
    '<cpd>': 'Gender=Neut|Number=Sing|Polarity=Pos|Variant=Short|VerbForm=Part|Voice=Pass',
    '<sp>': 'Number=Sing,Plur',
    '<indecl>': 'Case=Indecl',
    '<emph>': 'VerbType=Emph',
    '<lp>': 'VerbForm=Part',
    '<pii>': 'Tense=Imp',
    '<ref>': 'Valency=Refl',  # which tagset to follow for this?
    # check consistency with other tagsets (emphatic form of verb)
    #'<adv>+': 'Degree=Sup'


}


with open(r'E:\Lorenzo Tosi\OneDrive\Documenti\Program\NIS-FREQ\hrmorph.txt-yes-top10000', 'r', encoding='utf8') as f:
    analyses = []
    for line in f:
        analyses.append(line.split()[1].strip('^$'))

    for analysis in analyses:
        for aptag in udtags.keys():
            if aptag == '<n>' or aptag == '<vblex>' or aptag == '<adj>':
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
        
        rus: fac, cmp, dat? - поворот поворот NOUN Animacy=Inan|Case=Dat|Gender=Masc|Number=Sing
        fac - >  ?????????
        снялась	сняться	VERB	Aspect=Perf|Gender=Fem|Mood=Ind|Number=Sing|Tense=Past|VerbForm=Fin|Voice=Mid
        снялась	сняться	VERB	Aspect=Perf|Gender=Fem|Number=Sing<fac>|Tense=Past|Valency=1
        снялся	сняться	VERB	Aspect=Perf|Gender=Masc|Mood=Ind|Number=Sing|Tense=Past|VerbForm=Fin|Voice=Mid
        снялся	сняться	VERB	Aspect=Perf|Gender=Masc|Number=Sing<fac>|Tense=Past|Valency=1
        удалось	удаться	VERB	Aspect=Perf|Gender=Neut|Mood=Ind|Number=Sing|Tense=Past|VerbForm=Fin|Voice=Mid
        удалось	удаться	VERB	Aspect=Perf|Gender=Neut|Number=Sing<fac>|Tense=Past|Valency=1
        прожил прожить Aspect=Perf|Gender=Masc|Mood=Ind|Number=Sing|Tense=Past|VerbForm=Fin|Voice=Act
        прожил	прожить	VERB	Aspect=Perf|Gender=Masc|Number=Sing<fac>|Tense=Past|Valency=1
        пробыл	пробыть	VERB	Aspect=Perf|Gender=Masc|Mood=Ind|Number=Sing|Tense=Past|VerbForm=Fin|Voice=Act
        пробыл	пробыть	VERB	Aspect=Perf|Gender=Masc|Number=Sing<fac>|Tense=Past|Valency=1
        перебрался	перебраться	VERB	_	Aspect=Perf|Gender=Masc|Mood=Ind|Number=Sing|Tense=Past|VerbForm=Fin|Voice=Mid
        перебрался	перебраться	VERB	Aspect=Perf|Gender=Masc|Number=Sing<fac>|Tense=Past|Valency=1
        
        ces: nej<adv>+ -> Degree=Sup - nej<adv>+vysoký -, ne<adv>+ -> Polarity=Neg
        discard <indecl>
        hr: ref, lp
        '''

        surface_form = analysis.split('/')[0]
        # discard duplicates
        glosses = set(analysis.split('/')[1:])

        for gloss in glosses:
            lemma_and_pos = gloss.split('|')[0]
            gloss = '|'.join(sorted(gloss.split('|')[1:])).strip('|')
            # discard duplicated verb forms
            gloss = gloss.replace('VerbForm=Part|VerbForm=Vadv', '|' + 'VerbForm=Vadv')
            if '<' in gloss:
                print(surface_form, lemma_and_pos, gloss, sep='\t', file=open(r'E:\Lorenzo Tosi\OneDrive\Documenti\Program\NIS-FREQ\testfile.txt', 'a+', encoding='utf8'))

               
            # 13 Apr 2019 
#ADD:
# for rus:
    # <fac> = factual, (don't add this one наверн)
    # <itg> = interrogative (vblex, adv, adj)
    # cmp = Degree = Copm
    
# for hr: (croatian)
    # lp = ??
# also .conllu files (in chat)    
    
