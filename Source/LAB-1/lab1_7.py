import nltk
from nltk.tokenize import sent_tokenize,word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.util import ngrams
from collections import Counter
from nltk.collocations import *

file = open("E:\python\lab1_7.txt").read()

text = sent_tokenize(file)
temp = []
temp_n = []
sent_concat = ""
lemmatizer = WordNetLemmatizer()

for sentence in text:
    word = word_tokenize(sentence)
    for wd in word:
        lemmatization = lemmatizer.lemmatize(wd)
        temp.append(lemmatization)

trigrams = ngrams(temp,3)
trigram_measures = nltk.collocations.TrigramAssocMeasures()
finder = TrigramCollocationFinder.from_words(temp)
most_freq_trigram = sorted(finder.nbest(trigram_measures.raw_freq, 10))

for sentence in text:
    word_tok = word_tokenize(sentence)
    for wd in word_tok:
        lemmatization = lemmatizer.lemmatize(wd)
        temp_n.append(lemmatization)
        tri_gram = ngrams(temp_n,3)
        for t in most_freq_trigram:
            if t in tri_gram:
                if sentence not in sent_concat:
                    sent_concat = sent_concat + sentence
                else:
                    sent_concat = sent_concat
            else:
                sent_concat = sent_concat

print("sentence tokenized:",text)
print("word_tokenized and lemmatized :",temp)
print("most repeated trigrams:",Counter(trigrams))
print("top 10 of most repeated trigrams:",most_freq_trigram)
print("concatenated sentence:",sent_concat)