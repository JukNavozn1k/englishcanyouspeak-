import nltk
from nltk.corpus import wordnet
from translate import Translator
from googletrans import Translator # pip install googletrans==4.0.0-rc1
from wiki_ru_wordnet import WikiWordnet


nltk.download('wordnet') # база английских слов

translator = Translator()
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

def trs(text): # flag 0 -> ru to en else en to ru
    
    # Detect language of the text
    detected_lang = translator.detect(text).lang

    # Translate the text to English
    translation = translator.translate(text, src=detected_lang, dest='en')

    return translation.text




