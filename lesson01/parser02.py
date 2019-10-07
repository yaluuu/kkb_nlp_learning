#encoding=utf-8
import jieba as jeb
import pandas as pd
# raw_data = pd.read_csv('/mnt/disk1/data/learn/others/movie_comments.csv')
# print(raw_data[:1])


intab = ""
outtab = ""
trantab = str.maketrans(intab, outtab, "，")

test_str = "我去吃饭了，你呢？"

print (test_str.translate(trantab))

a=[('a',1),('b',4),('c',2)]
a.sort(key=lambda x: x[1], reverse=True)
print(a)
