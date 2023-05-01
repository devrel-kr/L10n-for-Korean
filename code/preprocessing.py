import pysubs2
import pandas as pd
import os
import re
import openpyxl
from openpyxl import Workbook
from konlpy.tag import Okt
from konlpy.tag import Kkma
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

wb = Workbook()
ws = wb.active
ws.append(['movie', 'start', 'end', 'dialogue', 'dialogue(no stopwords)'])

stop_words = ''
f = open("/home/vislab/Jiwon/Korean_quality/code/stopwords.txt", 'r')
while True:
    line = f.readline()
    if not line: break
    stop_words += line
stop_words = stop_words.split('\n')
f.close()

dir_path = "/home/vislab/Jiwon/Korean_quality/movie_data/미국"
movie_dic = {}
for (root, directories, files) in os.walk(dir_path):
    for file in files:
        if '.srt' in file:
            file_path = os.path.join(root, file)
            if file not in movie_dic: movie_dic[file] = {'start' : [], 'end' : [], 'dialogue' : [], 'dialogue(no stopwords)' : []}
            try:
                subs = pysubs2.load(f'{file_path}', encoding = "UTF-8")
                for i, line in enumerate(subs):
                    strl = str(line)
                    start_hour = strl[30 : 31]
                    start_min = strl[32 : 34]
                    start_sec = strl[35 : 37]
                    last_hour = strl[42 : 43]
                    last_min = strl[44 : 46]
                    last_sec = strl[47 : 49]
                    dia = line.text.replace('\\N', ' ')
                    movie_dic[file]['start'].append(start_hour + ':' + start_min + ':' + start_sec)
                    movie_dic[file]['end'].append(last_hour + ':' + last_min + ':' + last_sec)
                    movie_dic[file]['dialogue'].append(dia)
                    
                    # 형태소 분석 + 불용어 처리
                    okt = Okt()
                    word_tokens = okt.morphs(movie_dic[file]['dialogue'][-1])
                    result = [word for word in word_tokens if not word in stop_words]
                    movie_dic[file]['dialogue(no stopwords)'].append(" ".join(result))
                    if i == 0: ws.append([file, movie_dic[file]['start'][-1], movie_dic[file]['end'][-1], movie_dic[file]['dialogue'][-1], movie_dic[file]['dialogue(no stopwords)'][-1]])
                    else: ws.append(['', movie_dic[file]['start'][-1], movie_dic[file]['end'][-1], movie_dic[file]['dialogue'][-1], movie_dic[file]['dialogue(no stopwords)'][-1]])
                    print(result)
                    
            except: continue
wb.save("/home/vislab/Jiwon/Korean_quality/movie_data/미국/movie_data.xlsx")

