import pandas as pd
import gensim
import string
from gensim.models import Word2Vec
from gensim.models import Word2Vec, KeyedVectors

"""
# todo:
focus on one dataset only
parameter tuning for epoch
select only article content as input
"""

def clean_data(dataFilePath):
	with open(dataFilePath, 'r') as r:
		# df = pd.read_csv(r)
		# print('df[0]:', df[0])
		# print('df[1]:', df[1])
		# data = df['Article'].dropna()
		r = [line[:-1] for line in r]
		data = []
		exclude = set(string.punctuation)
		for line in r:
			# print('line: ')
			# print(line)
			line = line.translate(string.punctuation)
			line = line.lower()
			line = ''.join(ch for ch in line if ch not in exclude) # remove punc
			line = line.replace("\xa0", "").replace('"', "").replace("'", "")
			line = [x for x in line.split(" ") if x] # split into words
			if line:
				data.append(line)
	print(data)
	print('finished cleaning data.')
	print(len(data))
	return(data)

if __name__ == "__main__":
	dataFilePath = 'improvedData2.csv'
	modelName = '100epochimprovedData2'
	data = clean_data(dataFilePath)
	"""
	train new model based on improved data
	"""
	newModel = gensim.models.Word2Vec(
	    data,
	    size=150,
	    window=10,
	    min_count=1, 
	    # Default min_count in gensim's Word2Vec is set to 5. 
	    # If there is no word in your vocab with frequency greater than 4, 
	    # your vocab will be empty and hence the error.
	    workers=10)
	newModel.build_vocab(data, update=True)
	newModel.train(data, total_examples=len(data), epochs=10)
	newModel.save(modelName)

	"""
	create new 3300 model. 
	cannot use this model as a standalone model 
	since many common words not found in articles
	"""
	# model = gensim.models.Word2Vec(
	#     data,
	#     size=150,
	#     window=10,
	#     min_count=2,
	#     workers=10)