#!/usr/bin/env python3 
# Example use of spaCy to build a review vector
import spacy
import numpy as np
import sys
try:
    in_file = sys.argv[1]
    out_file = sys.argv[2]
except:
    print("usage: ./spacyDoc2Vec.py inputfile outputfile")
    sys.exit(1)

# Load Spacy's pre-trained word vectors
nlp = spacy.load('en_core_web_lg')

f = open(in_file,'r')
d = open(out_file, 'a+')

# Similar to customDoc2Vec
# Sum of word vectors in review
# Uses's spaCy's pre trained word vectors
count = 0
for line in f:
    count += 1
    split = line.rstrip().split('\t',1)
    try:
        tokens = nlp(split[1])
    except:
        continue
    s = tokens[0].vector
    for word in tokens[1:]:
        s = np.add(s,word.vector)
    output = split[0] + '\t' + str(list(s)).replace('\n', ' ');
    print('[Parsed Line: ' + str(count) + ']', end='\r')
    d.write(output)
    d.write('\n')
f.close()
d.close()
