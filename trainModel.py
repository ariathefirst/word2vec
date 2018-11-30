import pandas as pd
import gensim
from gensim.models import Word2Vec
from gensim.models import Word2Vec, KeyedVectors


model = Word2Vec.load("our_model")
model.wv.save_word2vec_format('new_model', binary=True)
print('saved new_model\n')

with open('articles3300 2.csv', 'r') as r:
	df = pd.read_csv(r)
	data = df['text'].dropna()
	res = []
	for line in data:
		res.append(line)
print(res)
"""
create new 3300 model
"""
# model = gensim.models.Word2Vec(
#     data,
#     size=150,
#     window=10,
#     min_count=2,
#     workers=10)
"""
train new model with 3300 sentences
"""
# model.train(data, total_examples=len(data), epochs=10)
# model.save('new_model')

"""c
train new model on top of our_model
"""
model.train(res, total_examples=len(res), epochs=10)
model.save("new_model")

"""
save 3300 sentences to csv
"""
