import re

listf=['mango','apple','banana','kiwi','efruit','imango']

for i in listf:
    if re.search('^[a,e,i,o,u]',i):
        print(i)

