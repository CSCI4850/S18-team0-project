#!/usr/bin/python3
# Example use of spaCy to build a review vector
import spacy
import numpy as np
import sys
filename = sys.argv[1]
# Load Spacy's word vectors
nlp = spacy.load('en_core_web_lg')
f = open(filename,'r')
d = open('data.txt', 'a+')
for line in f:
    split = line.rstrip().split('\t',1)
    try:
        tokens = nlp(split[1])
    except:
        continue
    s = tokens[0].vector
    for word in tokens[1:]:
        s = np.add(s,word.vector)
    output = str(s).replace('\n', ' ') + '\t' + split[0]
    d.write(output)
    ernt(output)
    d.write('\n')
f.close()
d.close()
