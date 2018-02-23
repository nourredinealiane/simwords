from nltk.corpus import stopwords
from nltk.corpus import wordnet
import numpy as np

stop = set(stopwords.words('french'))
print [i for i in  stop if len(wordnet.synsets(i)) != 0]


myfile = open('stopwordFrensh.txt', 'w')


for w in stop:
   myfile.write(w.encode('utf-8') + '\n')
	

myfile.close()

#print [i for i in sentence.lower().split() if i not in stop]


