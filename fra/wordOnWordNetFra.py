#!/usr/bin/python2.7
# coding: utf8

from nltk.corpus import stopwords
from nltk.corpus import wordnet
import numpy as np
import sys

filename = sys.argv[1] 
stop = set(stopwords.words('french'))

labels = np.genfromtxt(filename, usecols=(0),dtype=str) # loading the labels
words = [unicode(w, encoding='utf-8') for w in labels]

print len(words)

resultat ='resultats/wonwn' + filename[5:]
myfile = open(resultat, 'w')

i = 0
cpt = 0
for w in words:
 	s = wordnet.synsets(w, lang='fra')
	if ((len(s) != 0) & (len(w) > 1) & (w not in stop)):
		myfile.write(str(i) + ' \n')
 	  	cpt += 1
	i += 1
print i, cpt
myfile.close()

