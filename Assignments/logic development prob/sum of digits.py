def sum_of_digits(num):
    # Can you break the number into digits?
    # Decimal Number? Octal? Binary? -> Decimal
    # What is the Base of the Number? -> 10
    # What happens when you divide A Number by the Base?
    # What are the outputs of a division operation? Can they help you somehow?
    
    # 1234 / 10 = 123, 4 
    # 123  / 10 = 12 , 3
    # 12   / 10 = 1  , 2
    # 1    / 10 = 0  , 1
    
    # Set accumulated_sum = 0
    # Repeat UNTIL quotient is 0
        # divide the number by 10
        # Add the remainder to accumulated_sum
        # Store the quotient as the new number
    # Return the accumulated_sum
    pass
number = 1234
mod = 0
print(number)
for i in range(4):
    mod= number%10
    number = number // 10
    
    print(mod)
               
'''
number = 1234
expected = 10
actual = sum_of_digits(number
print('PASSED' if expected == actual else 'FAILED') 


number = 13221
expected = 9
actual = sum_of_digits(number)
print('PASSED' if expected == actual else 'FAILED')
'''