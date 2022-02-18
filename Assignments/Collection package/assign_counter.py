from collections import Counter as con

fr = open("news.txt", 'r', encoding = "utf-8")

data = fr.read()

c2 = con(data)
string1 = "aAeEiIoOuU"
print("Key's : value's")
for k,v in c2.items():
	# print(k)
	if k in string1:
		print(k.rjust(2).ljust(9),v)
