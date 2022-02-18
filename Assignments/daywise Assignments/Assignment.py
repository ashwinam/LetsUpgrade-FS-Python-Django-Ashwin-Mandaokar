# ASSIGNMENT NO.1
# MAKE A CLASS WHICH ACCEPTS LIST OF FRUITS & RETURN ALL THE FRUITS WHICH STARTS WITH VOWEL
# import re

# fruitList = ['mango', 'apple', 'banana', 'kiwi','Uglifruit']


# class listOfFruits:
#     def __init__(self, fruit_list):
#         self.fruit_list = fruit_list

#     def List_of_fruits(self):
#         for i in self.fruit_list:
#              if re.search('^[a,e,i,o,u][A,E,I,O,U]', i):
#                 print(i)
#                 # return i


# fruits = listOfFruits(fruitList)

# fruits.List_of_fruits()


# # ASSIGNMENT NO.2
# # MAKE A CLASS WHICH ACCEPTS JSON & GET ALL THE KEYS IN IT AND PRINT IT

# json_file={
#     "name":"ashwin",
#     "address":"chd",
#     "year":"2021"
# }

# class Json:
#     def __init__(self,json_dict):
#         self.json_dict=json_dict

#     def keysOfJson(self):
#         print('The following is the keys from above dictionery:-')
#         for i in self.json_dict.keys():
#             print(i)

# jsonFile=Json(json_file)
# jsonFile.keysOfJson()


# ASSIGNMENT NO.3
# MAKE A CLASS WHICH ACCEPTS 2 NUMBER (FLOAT OR INT) AS A PARAMETER _ADD,_SUBTRACT,_MULTIPLY,_DIVIDE AS PER THE FUNCTION CALL

# class calculator:
#     def addition(self,num1,num2):
#         return num1+num2

#     def subtraction(self,num1,num2):
#         return num1-num2

#     def multiplication(self,num1,num2):
#         return num1*num2

#     def divide(self,num1,num2):
#         return num1/num2

# calc=calculator()

# print(calc.addition(2,3))
# print(calc.subtraction(2,3))
# print(calc.multiplication(2,3))
# print(calc.divide(2,3))

# # ASSIGNMENT NO.4
# [1,2,3,4,5] reverse it without using .reverse or [::-1] method
# Example input list of numbers
# 
# Example input list of numbers
# numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# # Function takes a list as input
# def Reverse(numbers):
#       # Base case when the list is only one item
#       if (len(numbers)==1):
#          return numbers
#       # Otherwise
#       return Reverse(numbers[1:]) + numbers[0:1]

# # Test function
# print(Reverse(numbers))

# Example input list of numbers
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Get list length
L = len(numbers)

# i goes from 0 to the middle
for i in range(int(L/2)):
    # Swap each number with the number in 
    # the mirror position for example first 
    # and last
    n = numbers[i]
    numbers[i] = numbers[L-i-1]
    numbers[L-i-1] = n

# At this point the list should be reversed
print(numbers)

# listOfNum=[1,2,3,4,5]

# # for i in listOfNum:
# #     print(i)

# for i in range(len(listOfNum)+1):
#     if i>5:
#         print(i)
#     else:
#         break

# ASSIGNMENT 5
# randomList=[1,2,3,'4','67',56,'123','not an int','definitely not an int'] RETURN INT LIST [1,2,3,4,67,56,123]
# randomList=[1,2,3,'4','67',56,'123','not an int','definitely not an int']
# # randomList='ashwin'
# updatedList=[]
# for i in range(len(randomList)):
#     if i =='not an int':
#         break
#     # print(i)
#     # j+=i
#     updatedList.append(i)

# print(updatedList)

# # integer list
# finalList=[]
# for l in range(len(updatedList)):
#     print(int(updatedList[l]))
#     finalList.append(int(updatedList[l]))

# print(finalList)
