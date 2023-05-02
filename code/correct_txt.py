import chardet
import kss
import re
import pandas as pd
import os

input_folder = r"C:\Users\JIHAN\Desktop\새 폴더"
output_folder = r"C:\Users\JIHAN\Desktop\새폴더2"

for filename in os.listdir(input_folder):
    if filename.endswith(".txt"):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, "result_" + filename)

        with open(input_path, 'rb') as f:
            result = chardet.detect(f.read())

        with open(input_path, "r", encoding=result['encoding']) as f:
            text = f.read()
            text = text.replace("\n", " ")


        sentences = kss.split_sentences(text)

        '''
        pattern = r"(?<=[해|요|다|야|까|죠])\s+(?=[가-힣])"  # 특정 글자뒤에 공백이 등장하면 '.'추가
        text_with_dot = re.sub(pattern, ". ", text)
        
        pattern = r"(?<=[.?!])\s+(?=[가-힣])"
        sentences = re.split(pattern, text_with_dot)
        '''

        with open(output_path, "w", encoding=result['encoding']) as f:
            f.write('\n'.join(sentences))
