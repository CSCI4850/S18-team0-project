import re
import gensim

'''
longest = 0
l = None

with open('../TeamLTSM/reviews_Office_.txt') as file:
    for line in file:
        cur = len(re.sub(r'\W+', ' ', line).split(' ')) 
        if cur > longest:
            longest = cur
            #l = line
    print(longest)
    #print(l)
'''
'''
def TagDocument():
    longest = 5747 # for office reviews
    documents = []
    tags = []
    count = 0
    with open('../TeamLTSM/reviews_Office_.txt') as file:
        for line in file:
            
            #if count == 5:
            #    break
            
            #cur = re.sub(r'\W+', ' ', line).split(' ')
            #cur = line.split(' ')[1:]
            yield gensim.models.doc2vec.TaggedDocument(gensim.utils.simple_preprocess(line[14:]), [count])
            #author_tag = cur[0]
            #tags.append(author_tag) 
            #cur += [''] * (longest - len(cur))
            #documents.append(cur[1:])
            count += 1
        #print(documents)
        #print(tags)   
docs = list(TagDocument())
#print(docs)
print('Building vocab...')
model = gensim.models.doc2vec.Doc2Vec(vector_size=300, min_count=2, epochs=15)
model.build_vocab(docs)
print('Training...')
model.train(docs, total_examples=model.corpus_count, epochs=model.epochs)
model.save('officeModelTrained')
'''
model = gensim.models.doc2vec.Doc2Vec.load('officeModelTrained')
#print('Loaded Successfully')
#print(list(model.infer_vector(['hey', 'there'])))

with open('../../TeamLTSM/reviews_Office_.txt') as file:
    for line in file:
        cur = re.sub(r'\W+', ' ', line).split(' ')
        author = cur[0]
        review = [x for x in cur[1:] if x != '']
        print(author + '\t' + str(list(model.infer_vector(review))))
        #print(review)
        #print(list(model.infer_vector(review)))
