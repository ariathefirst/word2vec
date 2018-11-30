Open Jupyter Notebook (will be installed with Anaconda). Open Healthcare Word2Vec.ipynb through the Jupyter browser window that will open up once you start Jupyter (https://jupyter-notebook-beginner-guide.readthedocs.io/en/latest/) 

To run commands in Jupyter, press Shift+enter

### Our Model
- Our model was trained by op-eds scraped from Washington Post, CNN and Fox News on topic about Obama Care and Trump Care.
### Google's Model
- Google's model is a pre-trained through news from Google news, which contains more general information
To use Google's model, you need to download it: https://github.com/mmihaltz/word2vec-GoogleNews-vectors (GoogleNews-vectors-negative300.bin.gz) and rename it to
google.bin
It has to be in the same folder as the other files.

THings to do:
##### Most similar
- This function is trying to find the similarity between words relationship. For example, 
```python
our_model.most_similar(positive=['woman', 'female'], negative=['man'], topn=5)
```
- The code above was trying to find 'woman' to 'man' is like 'female' to '___'
- The idea behind this function is that words are represented as vector in a vector space. Therefore, we are able to coonect two vectors, i.e. 'woman' and 'man'. Then we will try to connect the target pair of words, i.e. 'female' and '___'. The line that is most parrallel to the line of 'woman' and 'man' should be the line we want. And the word that's connected to 'female' in this case, is the word we want.

##### Doesn't match & Similarity
- These two build in function are implemented by Genism, and we weren't able to figure out how the implementation actually works. However, based on our observation and experiment upon these functions, we believe it is implemented based on the calculation of cosine similarity.

##### Sentence similarity
- We calculated the average vector of a giving sentence by taking average on each element of the vector. To be notice, this method doesn't take order of words in account. For example, the average vector of sentence "This is a test" should be identical with "A test is this"

##### Test for vector addition and substraction
- Following the idea of Mikolov, we were trying to test vector addtion and substraction on both our model and Google's model. However, both models fail to demonstrate the result Mikolov suggested. For example, according to Mikolov, "king" - "man" + "woman" should be equal to "queen". However, the result from both models is not that similar to "queen". It seems like the substration isn't playing huge role in this test.

##### Models on politician related problems
- In the end, we tested our model again Google's model on politician related problems, which form most of our model's input. The result shows that our model performs better than Google's model on these problems.
