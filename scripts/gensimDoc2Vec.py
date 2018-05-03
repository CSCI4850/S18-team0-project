#!/usr/bin/env python3
import re
import gensim
import sys

# Get infile, outfile, and model name from cmdline
try:
    in_file = sys.argv[1]
    out_file = sys.argv[2]
    modelname = sys.argv[3]
except:
    print("usage: ./generateDoc2Vec inputfilename outputfilename modelname")
    sys.exit(1)
# Find the Longest review in the file
# Takes input file name as argument
# Returns count of longest review
def FindLongest(in_file):
    longest = 0
    ## Get the longest review in the file
    with open(in_file) as file:
        for line in file:
            cur = len(re.sub(r'\W+', ' ', line).split(' ')) 
            if cur > longest:
                longest = cur
    return longest

# Tag the documents with Gensim Doc2Vec
def TagDocument():
    longest = FindLongest(in_file)
    print(longest)# for office reviews
    documents = []
    tags = []
    count = 0
    with open(in_file) as file:
        for line in file:
            yield gensim.models.doc2vec.TaggedDocument(gensim.utils.simple_preprocess(line[14:]), [count])
            count += 1

docs = list(TagDocument())


# Build the Model
# Set vector_size, min_count, and epochs
ep = 15
v_size = 300
m_count = 2
print('Building Doc2Vec Model...')
model = gensim.models.doc2vec.Doc2Vec(vector_size=v_size, min_count=m_count, epochs=ep)
model.build_vocab(docs)

# Train the Model
print('Training...')
model.train(docs, total_examples=model.corpus_count, epochs=model.epochs)
model.save(modelname)

#Load the Model
try:
    model = gensim.models.doc2vec.Doc2Vec.load(modelname)
    print('Loaded Successfully')
except:
    print('Error loading model: exiting')
    sys.exit(1)
out = open(out_file, 'a')
with open(in_file) as file:
    for line in file:
        cur = re.sub(r'\W+', ' ', line).split(' ')
        author = cur[0]
        review = [x for x in cur[1:] if x != '']
        #print(author + '\t' + str(list(model.infer_vector(review))))
        out.write(author + '\t' + str(list(model.infer_vector(review))) + '\n')

print(out_file, ": vectors generated.", sep='')
