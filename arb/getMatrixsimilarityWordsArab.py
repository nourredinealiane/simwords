#!/usr/bin/python2.7
from nltk.corpus import wordnet
from itertools import product
import numpy as np
import sys

filename = sys.argv[1]
labels = np.genfromtxt(filename,usecols=(0),dtype=str)
cpt = 0
resultat ='resultats/simMatrix' + filename[5:] 
fi = open(resultat, 'w')

for i, wi in enumerate (labels[:-1]): 
   for wj in labels[i+1:]:
		syns1 = wordnet.synsets(unicode(wi, encoding='utf-8'), lang='arb')
		syns2 = wordnet.synsets(unicode(wj, encoding='utf-8'), lang='arb')
		fi.write(str(max((wordnet.wup_similarity(s1, s2) or 0) for s1, s2 in product(syns1, syns2))) + ' '+wi+' ' +wj+'\n')
		cpt +=1
			
	 

fi.close()

print 'cpt = ' +str(cpt) 





