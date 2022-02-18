import os
import datetime


print('===Welcome Stranger===')
print('Can i Get your Name?')
userName=input()
print(f'Thank you {userName},Have a Good Day!')

today=datetime.datetime(year=2021,month=5,day=25,hour=17,minute=55,second=50)
# today=today.strftime('%d-%m-%Y')
exactDate=datetime.datetime.now()
rightNow=datetime.datetime(year=2021,month=5,day=25,hour=17,minute=55,second=50)
rightNow=rightNow.strftime('%H:%M:%S')
print(f'Today date is {today}')
print(f'The time is {rightNow}')
oneDay=datetime.timedelta(days=1)
tomorrow=today+oneDay
tomorrow=tomorrow.strftime('%d/%m/%Y')
print(f'the next day is {tomorrow}')
# print('Today is your LU Class?')
# print('Type y/n :',end="")
# a=input()
# CWD=os.getcwd()
# while today.day!=exactDate:
#     createDirectory=os.mkdir(f'{CWD}/{today}')
#     today+=1

# print('Done')

# CWD=os.getcwd()
# print(CWD)
# setNewDirectory=os.chdir(f'{CWD}')
# print(setNewDirectory)
# print(CWD)

# OS MKDIR 
# createdDirectory=os.mkdir(f'{CWD}/{today}')
# removeDirectory=os.rmdir(f'{CWD}/{today}')