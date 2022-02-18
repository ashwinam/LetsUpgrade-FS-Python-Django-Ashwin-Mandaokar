randomList=[1,2,3,'4','67',56,'123','not an int','definitely not an int']
# randomList='ashwin'
updatedList=[]
for i in range(len(randomList)):
    if i =='not an int':
        break
    # print(i)
    # j+=i
    updatedList.append(i)

print(updatedList)

# integer list
finalList=[]
for l in range(len(updatedList)):
    print(int(updatedList[l]))
    finalList.append(int(updatedList[l]))

print(finalList)
