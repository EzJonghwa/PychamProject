from gensim.models import word2vec
from gensim.models import fasttext


data= word2vec.LineSentence('naver_movie.nlp')
w_model = word2vec.Word2Vec(data
                            ,vector_size=200 #임베팅 벡터 사이즈
                            ,window=8       #현재 단어를 기준으로 주변 단어 수
                            ,min_count=2    #최소 출현 수
                            ,sg=1)          #알고리즘 0 :CBOW, 1:skip-gram
f_model = fasttext.FastText(data
                            ,vector_size=200
                            ,window=8
                            ,min_count=2
                            ,sg=1)
w_model.save('w_embedding.model')
f_model.save('f_embedding.model')
while True:
    text = input("검색 단어")
    print('positive:', f_model.wv.most_similar(positive=[text]))
    print('negative:', f_model.wv.most_similar(negative=[text]))
