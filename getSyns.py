import nltk
from nltk.corpus import wordnet
from translate import Translator

from wiki_ru_wordnet import WikiWordnet


nltk.download('wordnet') # база английских слов

def contain(w,T):
    flag = False
    for t in T:
        if w in t or w == t: flag = True
    return flag

def ENget_syns(word):
        # find synonyms of a word
    synonyms = []
    for syn in wordnet.synsets(word):
        for lemma in syn.lemmas():
            synonyms.append(lemma.name())

    # remove duplicates and print the synonyms
    synonyms = list(set(synonyms))
    print(word,synonyms)
    return synonyms

def trs(word,flag=0): # flag 0 -> ru to en else en to ru
    if flag == 0: translator = Translator(from_lang='ru', to_lang='en')
    else: translator = Translator(from_lang='en', to_lang='ru')
    return translator.translate(word)
