# This is a guess the number game

import random

print('Hello, what is your name? ' )
name = input()

print('well!, ' +name+ ' choose the number between 1 to 20')


secretNumber = random.randint(1,20)
# print('DEBUG: the secret number is ' +str(secretNumber))



for guessTaken in range(1,4):
    print('Take a Guess')
    guess = int(input())
    if guess<secretNumber:
        print('The Guess is too Low')
    
    elif guess > secretNumber:
        print('The guess is too high')
        
    else :
        break
    
    
if guess == secretNumber:
    print(name + '!, your guess is right and it took ' + str(guessTaken) + ' guesses')
else:
    print('Nope ' +name+ ' the correct guess is '+ str(secretNumber)+' .')


    