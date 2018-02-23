#!/usr/bin/python2.7
# coding: utf8
from nltk.corpus import wordnet
import numpy as np
import sys

filename = sys.argv[1] 
labels = np.genfromtxt(filename, usecols=(0),dtype=str) # loading the labels
print len(labels)

resultat ='resultats/wonawn' + filename[5:]
myfile = open(resultat, 'w')
i = 0
cpt = 0
for w in labels:
	s = wordnet.synsets(unicode(w, encoding='utf-8'), lang='arb')
	if ((len(s) != 0) & (len(w) > 1)):
	  myfile.write(str(i) + '\n')
	  cpt += 1
        i += 1
print i, cpt
myfile.close()

#from AWNDatabaseManagement import wn as awn




