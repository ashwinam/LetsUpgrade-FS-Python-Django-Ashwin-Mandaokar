#23). Pattern program 4
'''
        *
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * *
'''
'''
number = 6
for i in range(number):
        for j in range(number - i - 1):
            print(" ", end=" ")

        for j in range(i + 1):
            print('*', end=" ")

        for k in range(i):
            print('*', end=" ")

        print()
'''
# Python program to print all
# prime number in an interval
# number should be greater than 1
'''
start = 1
end = 10

for i in range(start, end+1):
	if i > 1:
		for j in range(2, i):
			if(i % j == 0):
				break
		else:
			print(i)

'''
'''
year = 2016
if year % 4 == 0:
        print("this year is leap year")
elif year % 100 == 0:
    print("this year is leap year")
elif year % 400 == 0:
    print("this year is leap year")
else:
    print("This is not a leap year")
'''


#dumb code
'''
def prime_numbers(start,stop):
    temp=[]
    #print("The prime number are as follows:")
    for i in range(start,stop):
        for j in range(2,i):
            if i % j == 0:
                break
        else:
            temp.append(i)
    return temp



primeNumber = prime_numbers(2,100)

print(primeNumber)


num = 12
for i in primeNumber:
    if num % i == 0:
        #print(i)
        quotient = num // i
        num = num // i
        print(i)
        if quotient == i:
            print(i, end =" ")
'''
'''
# Python program to print prime factors

import math

# A function to print all prime factors of
# a given number n

def primeFactors(n):
    temp = []
    
    # Print the number of two's that divide n
    while n % 2 == 0:
        #print (2),
        temp.append(2)
        n = n // 2
        
    # n must be odd at this point
    # so a skip of 2 ( i = i + 2) can be used
    for i in range(3,int(math.sqrt(n))+1,2):
        
        # while i divides n , print i and divide n
        while n % i== 0:
            #print (i),
            temp.append(i)
            n = n / i
            
    # Condition if n is a prime
    # number greater than 2
    if n > 2:
        #print (n)
        temp.append(n)
    return temp
        
# Driver Program to test above function

def lcm(firstNumber,secondNumber,num1,num2):
    lcm = 1
    for i in firstNumber:
        for j in secondNumber:
            if i == j:
                lcm = lcm * j
    print (f"the lcm of ({num1}, {num2}) is {lcm}")

if __name__ == '__main__':
    number1=int(input("Enter the number1: "))
    number2=int(input("Enter the number2: "))

    #first_number = primeFactors(number1)
    #second_number = primeFactors(number2)
    
    lcm(primeFactors(number1),primeFactors(number2),number1,number2)
'''
input = 5
for row in range(input):
    for col in range(input-row):
        print("*", end = " ")
    print()






