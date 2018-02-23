from nltk.corpus import stopwords
from nltk.corpus import wordnet
import numpy as np
import sys

reload(sys)  
sys.setdefaultencoding('utf8')

filename = sys.argv[1] 
stop = set(stopwords.words('english'))
#print [i for i in  stop]

labels = np.genfromtxt(filename, usecols=(0),dtype=str) # loading the labels
print len(labels)

resultat ='resultats/wonwn' + filename[5:]
myfile = open(resultat, 'w')

i = 0
cpt = 0
for w in labels:
	s = wordnet.synsets(w)
	if ((len(s) != 0) & (len(w) > 1) & (w not in stop)):
		myfile.write(str(i) + '\n')
		cpt += 1
	i += 1
print i, cpt
myfile.close()

#print [i for i in sentence.lower().split() if i not in stop]


