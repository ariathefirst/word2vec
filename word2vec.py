from gensim import models
from scipy import spatial
import time
import numpy as np
import warnings
warnings.filterwarnings('ignore')

our_model = models.Word2Vec.load("our_model")
new_model = models.Word2Vec.load('new_model')

t1 = time.time()
t2 = time.time()
t2-t1

print('most_similar ex res:')
print(our_model.most_similar(positive=['women', 'female'], negative=['man'], topn=5))
print(new_model.most_similar(positive=['women', 'female'], negative=['man'], topn=5))

print('doesnt_match res')
print(our_model.doesnt_match("fair, just, equitable, favorable".split()))
print(new_model.doesnt_match("fair, just, equitable, favorable".split()))

print('most_similar res:')
print(our_model.most_similar(positive=['obamacare', 'republicans'], negative=['abortion'], topn=5))
print(new_model.most_similar(positive=['obamacare', 'republicans'], negative=['abortion'], topn=5))

print('similarity res:')
print(our_model.similarity('women', 'woman'))
print(new_model.similarity('women', 'woman'))




