#!/usr/bin/python2.7
from nltk.corpus import wordnet
from itertools import product
import numpy as np
import sys

def intersection_2_listes(L1, L2):
    """List[Int] * List[Int] -> List[Int]
    Retourne l'intersection des deux listes L1 et L2."""

    for n in L1:
        for x in L2:
            if n == x :
                return True
    
 
    return False

def listtostr(l):
    #""" list to string"""
     st = '[ '
     for w in l:
	st += w + ' '
     st += ']'
     return st

verbose = True
filename = sys.argv[1] 
clusters = []
with open(filename) as f:
    for line in f:
        clusters.append([unicode(w, encoding='utf-8') for w in line.strip().split(' ')])
k = 0
cpt = 0
n_good = 0
n_bad = 0
n_clusters = 0
sims = []
sims2 = []

resultat ='resultats/sim-' + filename[5:] 
fi = open(resultat, 'w')

fi.write('file_in :' + filename + '\n\n')
for cluster in clusters:
	n = len(cluster)
	k +=1
	if (n > 1):
         fi.write('cluster' +str(k)+'     :'+str(n) + '\n')
         n_clusters += 1
	 sim = []
	 n_comb = 0
	 for i, wi in enumerate (cluster[:-1]): 
	    for wj in cluster[i+1:]:
		syns1 = wordnet.synsets(wi, lang='arb')
		syns2 = wordnet.synsets(wj, lang='arb')
		sim.append(max((wordnet.wup_similarity(s1, s2) or 0) for s1, s2 in product(syns1, syns2)))
		cpt += 1
		if intersection_2_listes(syns1, syns2):
			n_comb += 1
			
	 avg = np.average(sim)
	 avg2 = (n_comb*2.0)/(n*(n-1))
	 sims.append(avg)
	 sims2.append(avg2)
	 fi.write(str(avg) + '\n')
	 fi.write(str(avg2) + '\n')
	 if (avg == 1):
	   st = listtostr(cluster)
	   fi.write('good :' + st.encode('utf-8') + '\n')
	   if (verbose):
	      print 'good :' , st
	   n_good += 1

         if (avg == 0):
	   st = listtostr(cluster)
	   fi.write('bad :' + st.encode('utf-8') + '\n')
	   if (verbose):
	      print 'bad :' , st
	   n_bad += 1

         fi.write('\n')
			
	

sim1 = np.average(sims)
sim2 = np.average(sims2)


fi.write('sim1 = ' + str(sim1) + '\n')
fi.write('sim2 = ' + str(sim2) + '\n')
fi.write('n_good = ' +str(n_good) + '\n')
fi.write('n_bad = ' +str(n_bad)+ '\n')
fi.write('nb_clusters_singleton = ' + str(k-n_clusters) + '/' +str(k)+ '\n')
fi.write('nb_combinaisons = ' +str(cpt) + '\n')

fi.close()

print('\nsim1 = ' + str(sim1) + '\n')
print('sim2 = ' + str(sim2) + '\n')
print 'cpt = ' +str(cpt) + ' n_good = ' +str(n_good) + ' n_bad = ' +str(n_bad)





