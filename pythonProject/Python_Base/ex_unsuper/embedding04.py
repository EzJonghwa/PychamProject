import numpy as np
from gensim.models import FastText

from sklearn.metrics.pairwise import cosine_similarity

fast_model = FastText.load_fasttext_format('cc.ko.300.bin')

sentence1 ='나는 오늘 영화를 봤다'
sentence2 ='오늘 난 영화를 보았다'
sentence3 ='영화 노잼'

# 문장 유사도 구하기

def sentence_vector(sentence, model):
    words = sentence.split()
    word_vectors =[]
    for word in words:
        if word in model.wv:
            word_vectors.append(model.wv[word])
    if len(word_vectors) ==0:
        return np.zeros(model.vector_size)
    return np.mean(word_vectors, axis=0)
# 문장 비교

def compare_sentence(doc1, doc2, model):
    vec1 = sentence_vector(doc1, model)
    vec2 = sentence_vector(doc2, model)
    sim = cosine_similarity([vec1],[vec2])
    return sim[0][0]

doc1_2 = compare_sentence(sentence1, sentence2, fast_model)
print (f"1:2 문장 유사도:{doc1_2}")
doc1_3 = compare_sentence(sentence1, sentence3, fast_model)
print (f"1:3 문장 유사도:{doc1_3}")
