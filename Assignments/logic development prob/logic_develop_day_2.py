arr = list(map(int, input().split(' ')))
temp = []
for i in range(len(arr)):
     if arr[i] %2 ==0:
         temp.append(arr)
print(temp)