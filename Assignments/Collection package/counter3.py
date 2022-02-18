# make a optimized counter programme
'''
if the programme file is larger in size then it take larger space in memory also.
'''

from collections import Counter as con

c1 = con()

fr = open("news.txt", 'r',encoding = 'utf-8')

for line in fr:
	c1.update(line.split())

print(c1)