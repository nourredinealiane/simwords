from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.corpus import wordnet
import numpy as np
import sys

filename = sys.argv[1] 

stop = set(stopwords.words('english'))
labels = np.genfromtxt(filename, usecols=(0),dtype=str) # loading the labels

resultat ='resultats/word2syn' + filename[5:]
myfile = open(resultat, 'w')

i = 0
for w in labels:
	s = wordnet.synsets(w)
	if ((len(s) != 0) & (len(w) > 1) & (w not in stop)):
		for syn in s: 
		  myfile.write(str(syn) + ' ')
		myfile.write('\n')
	i += 1
print i
myfile.close()




