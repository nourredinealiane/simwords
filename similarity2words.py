# coding: utf8

from nltk.corpus import wordnet
from itertools import product
import sys


syns1 = wordnet.synsets(sys.argv[1])
n1 = len(syns1)

syns2 = wordnet.synsets(sys.argv[2])
n2 = len(syns2)

print '---------------------------------------------'
if ((n1 != 0) & (n2 != 0)):
  best_wup = max((wordnet.wup_similarity(s1, s2) or 0, s1, s2) for s1, s2 in product(syns1, syns2))
  worst_wup = min((wordnet.wup_similarity(s1, s2) or 0, s1, s2) for s1, s2 in product(syns1, syns2))

  print 'le pire similarity = ' + str(worst_wup)
  print [w.encode('utf-8') for w in worst_wup[1].lemma_names()]
  print [w.encode('utf-8') for w in worst_wup[2].lemma_names()]
  print 'le dernier ancêtre commun est : ' + str(worst_wup[1].lowest_common_hypernyms(worst_wup[2]))
  print '---------------------------------------------'
  print 'le meilleur similarity = ' + str(best_wup)
  print [w.encode('utf-8') for w in best_wup[1].lemma_names()]
  print [w.encode('utf-8') for w in best_wup[2].lemma_names()]
  print 'le dernier ancêtre commun est : ' + str(best_wup[1].lowest_common_hypernyms(best_wup[2]))
  print '---------------------------------------------'

else:
  print 'impossible'

print '---------------------------------------------'







