from gensim import models
from scipy import spatial
import time
import numpy as np
import warnings

modelName = '100epochimprovedData2'
print('Model name is ', modelName)
warnings.filterwarnings('ignore')

our_model = models.Word2Vec.load("our_model")
modelName = models.Word2Vec.load(modelName)

t1 = time.time()
t2 = time.time()
 
print('doesnt_match res:')
print('our_model:')
print(our_model.doesnt_match("fair, just, equitable, favorable".split()))
print('newModel:')
print(modelName.doesnt_match("fair, just, equitable, favorable".split()))
print('\n')

print('doesnt_match res:')
print('our_model:')
print(our_model.doesnt_match("republican, trump, obama".split()))
print('newModel:')
print(modelName.doesnt_match("republican, trump, obama".split()))
print('\n')

print('most_similar ex res:')
print('our_model:')
print(our_model.most_similar(positive=['women', 'female'], negative=['man'], topn=5))
print('newModel:')
print(modelName.most_similar(positive=['women', 'female'], negative=['man'], topn=5))
print('\n')

print('most_similar res:')
print('our_model:')
print(our_model.most_similar(positive=['obamacare', 'abortion'], negative=['republicans'], topn=5))
print('newModel:')
print(modelName.most_similar(positive=['obamacare', 'abortion'], negative=['republicans'], topn=5))
print('\n')



