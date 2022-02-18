from importlib import reload
import os
import helperFunction
reload(helperFunction)


# print(os.getcwd()) #print current working directory

#print the today Date
print('The Today date is:')
print(helperFunction.today(),'\n')

#print the yesterday Date
print('The Yesterday date is:')
print(helperFunction.yesterday(),'\n')

#print the LastWeek 
print('The LastWeek date is:')
print(helperFunction.lastWeek(),'\n')