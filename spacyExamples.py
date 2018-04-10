#!/usr/bin/python3
# Example use of spaCy to build a review vector
import spacy
# Load Spacy's word vectors
nlp = spacy.load('en_core_web_lg')
# Grab a single line to test
testline = open('reviewsToys.txt').readline().rstrip().split('\t')
#Verify we got the line and split it
print("Reviewer ID:", testline[0])
print("Review:\n", testline[1])
#Convert the line into word vector objects
tokens = nlp(testline[1])
#See if they all have vectors, the normalization of the vector
#and if they are Out of Vocabulary
s = []
for word in tokens:
    print(word.vector)
    s.extend(word.vector)
print(s)
print(len(s))
