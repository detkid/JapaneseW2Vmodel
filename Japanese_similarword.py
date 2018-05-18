from gensim.models.word2vec import Word2Vec
model_path = './word2vec.gensim.model'
model = Word2Vec.load(model_path)

print(model.most_similar(positive='死', topn=20))
