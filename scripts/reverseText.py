#!/usr/bin/env python3
import sys
import string

# Check for valid command usage
try:
    in_file = sys.argv[1]
    out_file = sys.argv[2]
except:
    print("usage: ./reverseDocs.py inputfile outputfile")
    sys.exit(1)

# Reverse the Document tex for encoding
w = open(out_file , 'a')
f = open(in_file)
for line in f:
    line = line.split('\t')
    # Split the review and remove punctuation
    rev = line[1].rstrip()
    rev = rev.split()[::-1]
    rev = [w for w in rev]
    new = []
    for y in rev:
        x = "".join(c for c in y if c.isalnum())
        new.append(x)
    rev = " ".join(y for y in new)
    rev = "".join(c for c in rev if c not in string.punctuation)
    w.write(line[0] + '\t' + rev.rstrip())   
    w.write('\n')
f.close()
w.close()
