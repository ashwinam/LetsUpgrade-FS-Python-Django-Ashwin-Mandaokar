import os
import datetime

os.chdir('C:\\Users\\A_MAN\\Desktop\\Python & Django Full stack\\Study Materials')
CWD = os.getcwd()
# create a old folders for the previous class
folderName = ['25-05-2021', '27-05-2021', '29-05-2021', '01-06-2021',
              '03-06-2021','05-06-2021','06-06-2021','08-06-2021', '10-06-2021', '12-06-2021', '15-06-2021','19-06-2021']

tempMsg = 'Folder is exist'
print(CWD)
for folder in folderName:
    exitDirectory = os.path.isdir(f'{CWD}/{folder}')
    if exitDirectory == True:
        # if 'Folder is exist' in tempMsg:
        #     print('Folder is exist')
        break
    else:
        os.mkdir(f'{CWD}\\{folder}')

# For Current Classes
print('===Welcome Stranger===')
print('Can i Get your Name?')
userName = input()
print(f'Thank you {userName},Have a Good Day!')

# datetime module
today = datetime.datetime.now()
today = today.strftime('%d-%m-%Y')
rightNow = datetime.datetime.now()
rightNow = rightNow.strftime('%H:%M:%S')
print(f'Today date is {today}')
print(f'The current time is {rightNow}')


print("Is it Letsupgrade's class today?")
print('Type y/n :', end="")
inputResult = input()
exitDirectory = os.path.isdir(f'{CWD}/{today}')

if inputResult == 'y':
    if exitDirectory == True:
        print('Folder is Exist')
    else:
        createDirectory = os.mkdir(f'{CWD}/{today}')
else:
    print('Today is no Class,Come here by tomorrow!')

print('Thank you!')


# print(CWD)
# setNewDirectory=os.chdir(f'{CWD}')
# print(setNewDirectory)
# print(CWD)

# # OS MKDIR
# createdDirectory=os.mkdir(f'{CWD}/{today}')
# # removeDirectory=os.rmdir(f'{CWD}/{today}')
