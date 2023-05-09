from pykospacing import Spacing
import os
import pandas as pd

spacing = Spacing()

folder_path = r"C:\Users\JIHAN\Desktop\후"

results = []
count = 0;

for file_name in os.listdir(folder_path):
    if file_name.endswith(".txt"):
        count += 1
        print(count)
        with open(os.path.join(folder_path, file_name), "r", encoding="utf-8") as f:
            sentences = f.readlines()[3:]
        incorrect_count = 0
        for sentence in sentences:
            spaced_sentence = spacing(sentence)
            if len(sentence.strip()) != len(spaced_sentence.strip()):
                incorrect_count += 1
        result = {"file_name": file_name, "incorrect_ratio": incorrect_count/len(sentences)}
        results.append(result)

df = pd.DataFrame(results)
df.to_excel("result.xlsx", index=False)


