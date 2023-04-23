import pandas as pd
import pandas_profiling
import csv
from collections import Counter

data = pd.read_csv("/home/vislab/Jiwon/Korean_quality/movie_data/미국/movie_data2.csv", encoding = "utf-8")
pr = pandas_profiling.ProfileReport(data)
print(pr)