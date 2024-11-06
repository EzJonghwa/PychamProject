from gensim.models import FastText, Word2Vec
from gensim.models import Word2Vec
# load_model = FastText.load('./f_embedding.model')
# load_model = Word2Vec.load('./w_embedding.model')
# print('positive:', load_model.wv.most_similar(positive=['이정재','재미','최민식']))
# print('negative:', load_model.wv.most_similar(negative=['이정재','재미','최민식']))

from gensim.models import FastText
model = FastText.load_fasttext_format('cc.ko.300.bin')
while True:
    text = input("단어 2개").split()
    print(model.wv.similarity(text[0],text[0]))