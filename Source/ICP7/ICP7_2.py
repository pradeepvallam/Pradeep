import nltk
from nltk.tokenize import sent_tokenize,word_tokenize
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from nltk import wordpunct_tokenize,pos_tag,ne_chunk
from nltk.util import ngrams
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')

file = open("E:\input.txt").read()
#Tokenization
stokens = sent_tokenize(file)
print("sentence: ", stokens)

for sentence in stokens:
    wtokens = word_tokenize(sentence)
print("words:", wtokens)

#POS
pos = nltk.pos_tag(wtokens)
print("pos: ", pos)

#Stemming
pstem = PorterStemmer()
for words in wtokens:
    print(pstem.stem(str(words)))


#lemmatization
lemm = WordNetLemmatizer()
for words in wtokens:
    print(lemm.lemmatize(str(words)))


#named entity frecognition
ner = ne_chunk(pos_tag(wordpunct_tokenize(str(stokens))))
print("NER: ", ner)

#trigram
tgram = []
trigram = ngrams(wtokens,3)
for i in trigram:
    tgram.append(i)
print("trigrams: ", tgram)

