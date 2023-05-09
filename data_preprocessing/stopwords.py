import os
import pandas as pd
from konlpy.tag import Okt
import re

okt = Okt()

with open("stopwords.txt", "r", encoding="utf-8") as stopword_file:
    stopword_list = stopword_file.read().splitlines()

# 파일경로
dirpath = r"C:\Users\JIHAN\Desktop\후"

all_data = {
    "filename": [],
    "characters": [],
    "lines": [],
    "stopWords": []
}
count = 0
pattern = r"[^\w\s.,?!-]"
for filename in os.listdir(dirpath):
    count += 1
    print(count)
    if filename.endswith(".txt"):
        filepath = os.path.join(dirpath, filename)

        morpheme_list = []
        with open(filepath, "r", encoding="utf-8") as f:
            lines = f.readlines()
            for line in lines[3:]:
                line = re.sub(pattern, "", line)
                line = line.strip()
                morphemes = okt.morphs(line)
                morpheme_list.extend(
                    [morpheme for morpheme in morphemes if morpheme not in stopword_list and morpheme != ''])

        data = {
            "filename": [filename],
            "characters": [len(morpheme_list)],
            "lines": [len(lines) - 3],
            "stopWords": [', '.join([morpheme for morpheme in morpheme_list if morpheme not in stopword_list and morpheme != ''])]
        }
        df = pd.DataFrame(data)

        all_data["filename"].append(filename)
        all_data["characters"].append(len(morpheme_list))
        all_data["lines"].append(len(lines) - 3)
        all_data["stopWords"].append(', '.join([morpheme for morpheme in morpheme_list if morpheme not in stopword_list and morpheme != '']))

all_df = pd.DataFrame(all_data)
all_df.to_excel("output.xlsx", index=False)
