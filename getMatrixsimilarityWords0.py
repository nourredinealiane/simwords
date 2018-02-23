from nltk.corpus import wordnet
from itertools import product
import numpy as np
import sys

filename = sys.argv[1]
labels = np.genfromtxt(filename,usecols=(0),dtype=str)
cpt = 0
resultat ='resultats/simMatrix0' + filename[5:] 
fi = open(resultat, 'w')

for i, wi in enumerate (labels[:-1]): 
   for wj in labels[i+1:]:
		syns1 = wordnet.synsets(wi)
		syns2 = wordnet.synsets(wj)
		fi.write(str(wordnet.wup_similarity(syns1[0], syns2[0])) + ' ')
		cpt +=1
			
	 

fi.close()

print 'cpt = ' +str(cpt) 





