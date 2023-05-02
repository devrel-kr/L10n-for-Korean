from pykospacing import Spacing
import os
import pandas as pd

spacing = Spacing()

# 폴더 경로
folder_path = r"C:\Users\JIHAN\Desktop\처리후\통합데이터셋"

# 결과를 저장할 리스트 초기화
results = []
count = 0;
# 폴더 내에 있는 txt 파일들에 대해 수행
for file_name in os.listdir(folder_path):
    if file_name.endswith(".txt"):
        count+=1
        print(count)
        with open(os.path.join(folder_path, file_name), "r", encoding="utf-8") as f:
            sentences = f.readlines()
        incorrect_count = 0
        for sentence in sentences:
            spaced_sentence = spacing(sentence)
            if(len(sentence.strip()) != len(spaced_sentence.strip())):
                incorrect_count += 1
        result = {"file_name": file_name[10:], "incorrect_ratio": incorrect_count/len(sentences)}
        results.append(result)

# 결과를 엑셀 파일로 저장
df = pd.DataFrame(results)
df.to_excel("result.xlsx", index=False)

