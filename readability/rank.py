from collections import defaultdict
from konlpy.tag import Mecab
import os
import pandas as pd

mecab = Mecab(dicpath=r"C:\mecab\mecab-ko-dic")

with open('stopwords.txt', 'r', encoding='utf-8') as f:
    stopwords = [word.strip() for word in f]

tokenized_data = defaultdict(list)
dir_path = r'C:\Users\JIHAN\Desktop\후'

count = 0
for file_name in os.listdir(dir_path):
    count += 1
    print(count)
    file_path = os.path.join(dir_path, file_name)
    with open(file_path, 'r', encoding='utf-8') as f:
        data = f.read()
    for sentence in data.split('\n'):
        for pos in mecab.pos(sentence):
            if pos[1] in ['NNG', 'NNP', 'VV', 'VA', 'MAG']:
                if pos[1] in ['VV', 'VA']:
                    token = pos[0] + '다'
                else:
                    token = pos[0]
                if token not in stopwords:
                    tokenized_data[file_name].append(token)

rows = []
for file_name, tokens in tokenized_data.items():
    tokens_str = ', '.join(tokens)
    rows.append({'File Name': file_name, 'Rank Result': 0, 'Tokens': tokens_str})
df = pd.DataFrame(rows, columns=['File Name', 'Rank Result', 'Tokens'])

rank_df = pd.read_excel('어휘 등급.xlsx')

count = 0
for i, row in df.iterrows():
    tokens = row['Tokens'].split(', ')
    rank_result = 0
    count += 1
    print(count)
    for token in tokens:
        token_info = rank_df[(rank_df['어휘'] == token) & (rank_df['품사'] == mecab.pos(token)[0][1])]
        if not token_info.empty:
            rank = token_info['수준'].iloc[0]
            rank_result += int(rank)
        else:
            rank_result += 1
    rank_result /= len(tokens)
    df.at[i, 'Rank Result'] = rank_result


df.to_excel('rank_result.xlsx', index=False)
