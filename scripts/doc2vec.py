#!/usr/bin/env python3
import gensim
import numpy as np
import os

model = gensim.models.KeyedVectors.load_word2vec_format('./GoogleNews-vectors-negative300.bin', binary=True)

filename = input("[Choose file]: ")
outputfile = input("[Name output file]: ")

with open(filename) as file:
    count = 0
    for line in file:
        line = line.split('\t')
        reviewerID = line[0]
        review = line[1]
        
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
        os.system('echo "' + str(arr.tolist()) + '\t"' + reviewerID + ' >> ' + outputfile)
