
#%%
get_ipython().system('git clone "https://github.com/wswu/coglust.git"')
get_ipython().system('wget "https://db.panlex.org/panlex_lite.zip"')
get_ipython().system('unzip panlex_lite.zip')
get_ipython().system('pip install pycountry')
get_ipython().magic('cd coglust')
get_ipython().system('mkdir dicts')
get_ipython().system('touch wikitionary_langs.txt')

get_ipython().system('sed -i -e "s|/home/wwu/coglust/|/content/coglust/|g" createdicts.py')
get_ipython().system('sed -i -e "s|/export/a08/wwu/res/|/content/|g" createdicts.py ')
get_ipython().system('sed -i -e "s|/export/a08/wwu/dicts/|dicts/|g" createdicts.py ')
get_ipython().system('sed -i -e "s|~/coglust/|/content/coglust/|g" createdicts.py')
get_ipython().system('sed -i -e "s|for langcode in lang_name|for langcode in \\[str(n) for n in \\[382,211,666,579,304,101,610\\]\\]|" createdicts.py')

get_ipython().system('sed -i -e "s|langcodes.macrolang(lang)|lang|g" gather_from_dicts.py')
get_ipython().system('sed -i -e "s|langcodes.microlangs\\[lang\\]|\\[\\]|g" gather_from_dicts.py')
get_ipython().system('sed -i -e "s|import langcodes|# import langcodes|" gather_from_dicts.py')
get_ipython().system('sed -i -e "s|gather_from_wiktionary(langs)|\\[\\]|" gather_from_dicts.py')
get_ipython().system('sed -i -e "s|def \\[\\]|def gather_from_wiktionary(langs)|g" gather_from_dicts.py')

get_ipython().system('sed -i -e "s|wiktionary_location|# wiktionary_location|g" config.py')
get_ipython().system('sed -i -e "s|panlex_location|# panlex_location|g" config.py')

#%%
get_ipython().system('python3 createdicts.py')
get_ipython().system('python3 gather_from_dicts.py wikitionary_langs.txt gathered.txt --gathered_panlex dicts')
get_ipython().system('python3 cluster.py gathered.txt lev 0.4 unweighted-0.4 --linkage single')
