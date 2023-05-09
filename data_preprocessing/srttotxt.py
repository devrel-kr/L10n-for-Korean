import os
import pysrt
import chardet
import re

#파일경로
path = r'C:\Users\JIHAN\Desktop\처리전\영국자막파일\자막(81~160)'

for file in os.listdir(path):
    if file.endswith('.srt'):
        subs = None
        file_path = os.path.join(path, file)
        with open(file_path, 'rb') as f:
            result = chardet.detect(f.read())
            encoding = result['encoding']
        subs = pysrt.open(file_path, encoding=encoding)
        txt_file = os.path.splitext(file_path)[0] + '.txt'
        with open(txt_file, 'w', encoding='utf-8') as f:
            for index, sub in enumerate(subs):
                text = sub.text
                text = re.sub(r'<.*?>', '', text)
                text = text.replace('-', ' ')
                text = text.replace('&nbsp;', ' ')
                f.write(text + '\n')

