from collections import Counter as con

fr = open("news.txt", 'r', encoding = "utf-8")

# data = fr.read()
#  it return each characters
data = fr.read().split() # it return a list


c2 = con(data)
print(c2)
