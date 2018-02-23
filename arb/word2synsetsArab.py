#!/usr/bin/python2.7
from nltk.corpus import wordnet
import numpy as np

labels = np.genfromtxt('data/vectorsGrapavecOnAWN',usecols=(0),dtype=str) # loading the labels
myfile = open('word2synArab.txt', 'w')

i = 0
for w in labels:
	s = wordnet.synsets(unicode(w, encoding='utf-8'), lang='arb')
	myfile.write(w + ' : ')
	for syn in s: 
	  myfile.write(str(syn) + ' ')
	myfile.write('\n')
	i += 1
print i
myfile.close()




