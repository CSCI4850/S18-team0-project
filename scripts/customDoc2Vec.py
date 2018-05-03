#!/usr/bin/env python3
import gensim
import numpy as np
import os
import string
import sys


try:
    filename = sys.argv[1]
    outputfile = sys.argv[2]
except:
    print("usage: ./customDoc2Vec inputfilename outputfilename")
    sys.exit(1)

# Use pre downloaded model format
# must have in local dir to use
model = gensim.models.KeyedVectors.load_word2vec_format('./GoogleNews-vectors-negative300.bin', binary=True)

# Custom Word 2 Vec generation using vocabular/model from Google News
# Removes everything that isn't alphanumeric
# Document vector is the sum of the word2vec vectors
with open(filename) as file:
    count = 0
    for line in file:
        line = line.split('\t')
        reviewerID = line[0]
        review = line[1]
        review = "".join(w for w in review if w not in string.punctuation)
        review = " ".join(w for w in review.split()[::-1])
        arr = np.zeros(300)
        for word in review.split():
            try:
                if word[-1].isalpha():
                    arr = np.add(arr, model[word])
                else:
                    arr = np.add(arr, model[word[:-1]])
            except:
                pass
        print('[Parsed Line: ' + str(count) + ']', end='\r')
        count += 1
        os.system('echo "' + reviewerID + '\t' + str(arr.tolist()) + '" >> ' + outputfile)
