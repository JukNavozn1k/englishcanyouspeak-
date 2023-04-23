from nltk.corpus import wordnet
import nltk
word = 'fall'
#nltk.download('wordnet')

synonyms = []
for syn in wordnet.synsets(word):
    for lemma in syn.lemmas():
        synonyms.append(lemma.name())

print(set(synonyms))
