print('Learn about Dictioneries!')

student = {'name':'john', 'age':26, 'courses':['Python','Django']}

student['phone'] = 99999999
print(student.get('phone', 'Not Found!'))
# print(student)

# update method , it's handy when you want to update more than one entry

student.update({'name':'ashwin','phone':5555555, 'abc':'def'}) # overwrite the values of key
# print(student)

# delete the key value pair

# del student.get('age') # SyntaxError: cannot delete function call
del student['age']
# age = del student['age'] # couldn't store on variabe what we delete
# using pop method we seee what we delete by storing on a variable

abc = student.pop('abc')
# print(student)
# print(abc)

# let's loop through the dictionery

# print(student.keys())
# print(student.values())
# print(student.items())

# for key in student.keys():
#     print(key)
# for key in student.values():
#     print(key)
# for key in student.items():
#     print(key[0],key[1])
# for key,value in student.items():
#     print(key, value)

# for key in student.keys():
#     print(student.get(key))
#     print(student[key])

#  create a new dictionery using dict function

newDict = dict(name='rahul', age = 24, city='chd') # in here we don't need to give quotes in keys

# print(newDict)

# newDict.popitem() # it removes last entry

# copy the Dictioneries
# Using assignment operator

# newDict_cpy = newDict
# print(newDict_cpy)
# print(newDict)

# with assignment operator it changes original dictionary also so be carefull!!!

# newDict_cpy['phone'] = 5555
# print(newDict_cpy)
# print(newDict)

# for copy the dictionery with no harm use .copy() or dict()
# using .copy()
# newDict_cpy = newDict.copy()
# newDict_cpy['phone'] = 5555

# print(newDict_cpy)
# print(newDict)

# using dict()
# newDict_cpy = dict(newDict)
# newDict_cpy['phone'] = 5555

# print(newDict_cpy)
# print(newDict)

# merge two dictioneries using update function but here it overwrite the available values of key







