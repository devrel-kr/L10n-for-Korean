import os
import chardet
import codecs
from bs4 import BeautifulSoup

# 파일경로
path = r'C:\Users\JIHAN\Desktop\처리전\영국자막파일\자막(81~160)'

for file in os.listdir(path):
    if file.endswith('.smi'):
        file_path = os.path.join(path, file)
        with open(file_path, 'rb') as f:
            result = chardet.detect(f.read())
            encoding = result['encoding']
        with codecs.open(file_path, 'r', encoding=encoding) as f:
            soup = BeautifulSoup(f, 'html.parser')
        text = soup.get_text()
        korean_text = ''.join(char for char in text if char.isalnum() or char.isspace())
        txt_file = os.path.splitext(file_path)[0] + '.txt'
        with open(txt_file, 'w', encoding='utf-8') as f:
            f.write(korean_text)
