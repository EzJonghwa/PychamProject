# pip install  gensim
# pip install konlpy
import csv

from konlpy.tag import Okt


f = open('./data/ratings_train.txt', 'r', encoding='utf-8')
reader = csv.reader(f, delimiter='\t')
data = list(reader)
f.close()
# 한국어 파서
okt = Okt() # 자연어 한국어 분석해줌.
result = []
for line in data:
    d = okt.pos(line[1], norm=True, stem=True)
    r = []
    for word in d:
        if not word[1] in ['Josa', 'Eomi', 'Punctuation']:
            r.append(word[0])
    rl = (" ".join(r)).strip()
    result.append(rl)
print(result)
f = open("naver_movie.nlp", 'w', encoding='utf-8')
f.write('\n'.join(result))
print('save data')
f.close()