from collections import defaultdict
from konlpy.tag import Mecab
from gensim.models import Word2Vec

mecab = Mecab(dicpath=r"C:\mecab\mecab-ko-dic")

import os

tokenized_data = []
dir_path = r'C:\Users\JIHAN\Desktop\처리후\통합데이터셋'
for file_name in os.listdir(dir_path):
    file_path = os.path.join(dir_path, file_name)
    with open(file_path, 'r', encoding='utf-8') as f:
        data = f.read()
    for sentence in data.split('\n'):
        for pos in mecab.pos(sentence):
            if pos[1] in ['NNG', 'NNP', 'VV', 'VA']:
                if pos[1] in ['VV', 'VA']:
                    tokenized_data.append(pos[0] + '다')
                else:
                    tokenized_data.append(pos[0])


# 모델 학습
#model = Word2Vec(sentences=[tokenized_data], vector_size=100, window=5, min_count=1, workers=4, sg=1)
# 모델 저장
#model.save('jihan_model')

model = Word2Vec.load('jihan_model')
similar_words = model.wv.most_similar('사람')
print(similar_words)

