#!/usr/bin/python2.6
# coding: utf8

from nltk.corpus import wordnet as wn
from itertools import product
import sys

word_synsets = wn.synsets(u'ضِفَّة', lang='arb')
if word_synsets: # False if word_synsets is an empty list
    word_hyp = word_synsets[0].hypernyms()
    if word_hyp: # False if word_hyp is an empty list
        print(word_hyp[0].lemma_names(lang='arb'))
    else:
        print('first item in ضِفَّة synset has no hypernym(s)')
else:
    best = unicode('synset for ضِفَّة returned no resul', encoding='iso8859')
    print (best)





