# Let's make a To Do app
'''
What is To Do App?
:- It's a list of task you need to complete , or things that you want to do...
Requirements:-
1.Its a CRUD(Create, Read, Update, Delete) App
2.user able to add, see, update and delete the to dos
3. for that need to create 4 functions[done]
4. in here i am using Dictionery for crud operation
    -create a show to dos
    -create a add todos
    -create a update todos
    -create a delete todos

Improvement-
1. improve the UI[done]
2. in show function use three views
    -newly created todos, in process todos and completed todos[done]
    for moving entries i use pop method and list for using same dictionery.[done]
3. use input validation using try and except[done]
4. use additional things like dates and use pickle to store the data

Bugs:
1. in update method list ke alava agar koi number deta hu to wo new add kar leta hai.
    -for that need to specify the keys values, iske alava use nahi kr sakate[done]
2. in delete method need to give input validation[done]
3. after deleting the task sr.no still same it need to be changed with there respective numbers.
4. multiple entries it messed the views[done]
5. whenever i moved my entries my views messed up
    -what i need is first loop must be completed then second loop start with endline?
        -lets try with the 2 d array(but the 2d array print with the rows)
    - i think i need to use the different list for inprogress and completed tasks
'''
# print("Let's Create a App")

def workInProgress():
    push_entries = int(input('Enter the number to transfer into In progress: '))
    value = toDo.pop(push_entries)
    inProgress.append(value)
    

def newlyAddedViews():
    for key, values in toDo.items():
        print(f'{key} | {values}'.center(27),end='')
    inProgressView()

def inProgressView():
    for value in range(len(inProgress)):
        print(f"{value} | {inProgress[value]}".center(23))

def views():
    newlyAddedViews()



def toDoView():
    while (True):
        print()
        print('To Do list'.center(25),end='')
        print('In Progress'.center(25),end='')
        print('Completed Task'.center(25))
        print('**************'.center(25),end='')
        print('***************'.center(25),end='')
        print('******************'.center(25))
        print('Sr.No | ToDo'.center(25),end='')
        print('Sr.No | ToDo'.center(25),end='')
        print('Sr.No | ToDo'.center(25))
        print('--------------'.center(25),end='')
        print('--------------'.center(25),end='')
        print('--------------'.center(25))
        if inProgress:
            views()
        else:
            for key, values in toDo.items():
                print(f'{key} | {values}'.center(27))
        print()
        print('Choose below options 1 to 3'.center(60))
        print('1.Put task in Progress, 2.Put task In Completed, 3.quit the option')
        userChoice = int(input('Enter the Task: '))
        if userChoice == 1:
            print('In Progress')
            workInProgress()
        if userChoice == 2:
            print("Complete Task List")
        if userChoice == 3:
            print('Exit...')
            break

def show():
    if len(toDo) != 0:
        toDoView()
    else:
        print('theres No To Do In DataBase, Press 1 for make one.')

def add():
    user_input = input('Enter the Task: ')
    for keyName in range(1,10):
        if keyName not in toDo.keys():
            toDo[keyName] = user_input
            return toDo


def update():
    print('Use the key number for Update')
    show()
    keyUpdate = int(input("Enter the Number from above todo's that you want to update: "))
    for keys in toDo.keys():
        if keyUpdate == keys:
            toDo[keyUpdate] = input('Enter the Task: ')
            break
        else:
            print('Its Not Available in Todos , use the sr.no from above')
            break

def delete():
    print('Use the Number from Sr.No for Delete')
    show()
    deleteKeyNum = int(input("Enter the Number from above todo's that you want to delete: "))
    if deleteKeyNum in toDo.keys():
        del toDo[deleteKeyNum]
        print('selected Task Deleted from Database')
    else:
        print('Use the number from sr.no')

if __name__=="__main__":
    toDo = {}
    inProgress = []
    completedTask = []
    print('''
    Welcome to the Apna Kam Manage KarneWala!
        Choose Your Option from 1 to 5...

            1. Add the To Do
            2. Show the To Do
            3. Edit The To Do
            4. Delete The To Do
            5. Exit the App
    ''')
    while (1):
        print()
        try:
            user_choice = int(input('Enter Your Choice: '))
            print()
            if user_choice == 1:
                add()
            if user_choice == 2:
                show()
            if user_choice == 3:
                update()
            if user_choice == 4:
                delete()
            if user_choice == 5:
                print('Exit...')
                break
        except:
            print('Give the correct Choice, Between 1 to 5.')
        
        print()
        print('1. Add the To Do, 2. Show the To Do, 3. Edit The To Do, 4. Delete The To Do, 5. Exit the App')

