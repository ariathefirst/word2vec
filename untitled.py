import pandas as pd
import gensim
from gensim.models import Word2Vec
from gensim.models import Word2Vec, KeyedVectors


model = Word2Vec.load("our_model")

with open('articles3300 2.csv', 'r') as r:
	df = pd.read_csv(r)
	data = df['text'].dropna()
	res = []
	for line in data:
		res.append(line)
print(res)

"""
train new model on top of our_model
"""
model.train(res, total_examples=len(res), epochs=10)
model.save("new_model")

