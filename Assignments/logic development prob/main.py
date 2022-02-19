def isEqual(expected, actual):
    import random
    happy_symbols = ['🥳', '🎉', '🥰', '🤩', '😍', '😊', '😌' ]
    sad_symbols =   ['😱', '🤮', '😪', '😵', '🤔', '😑']
    if expected == actual:
        first_emoji = '✅'
        message = 'Test Passed'
        last_emoji = happy_symbols[random.randint(0, len(happy_symbols) - 1)] 
    else:
        first_emoji = '❌'
        message = 'Test Failed'
        last_emoji = sad_symbols[random.randint(0, len(sad_symbols) - 1)] 

    print('''
-------[ Test Case ]-------
Expected: {}
Received: {}
Verdict: {}  {} {}
'''.format(expected, actual, first_emoji, message, last_emoji))

""" Python Keywords: is try except raise from import global lambda yield """



"""Pattern Problem"""
def first_pattern(number):
    """
    1 |   *
    2 |   * *
    3 |   * * *
    4 |   * * * *
    5 |   * * * * *
    """
    for i in range(number):
        for column in range(i+1):
            print('*', end=" ")
        print()


def second_pattern(number):
    """
    1 |   * * * * *
    2 |   * * * *
    3 |   * * *
    4 |   * *
    5 |   *
    """
    for i in range(number, 0, -1):
        for column in range(0, i):
            print("*", end=" ")
        print()


def third_pattern(number):
    """
    *
    * *
    * * *
    * * * *
    * * * * *
    * * * *
    * * *
    * *
    *
    """
    first_pattern(number)
    second_pattern(number - 1)


def fourth_pattern(number):
    """
            *
          * *
        * * *
      * * * *
    * * * * *
    """
    for i in range(number):
        for j in range(number - i - 1):
            print(" ", end=" ")

        for j in range(i + 1):
            print('*', end=" ")
        print()


def fifth_pattern(number):
    """
            *
          * * *
        * * * * *
      * * * * * * *
    * * * * * * * * *
    """
    for i in range(number):
        for j in range(number - i - 1):
            print(" ", end=" ")

        for j in range(i + 1):
            print('*', end=" ")

        for k in range(i):
            print('*', end=" ")

        print()


def sixth_pattern(number):
    """
    * * * * *
      * * * *
        * * *
          * *
            *
    """
    for i in range(number, 0, -1):
        for j in range(number - i):
            print(" ", end=" ")

        for j in range(i ):
            print('*', end=" ")

        print()


def seventh_pattern(number):
    """
    * * * * * * * * * 
      * * * * * * *
        * * * * * 
          * * * 
            *
    """
    for i in range(number, 0, -1):
        for j in range(number - i):
            print(" ", end=" ")

        for j in range(i ):
            print('*', end=" ")
            
        for k in range(i-1):
            print("*",end=" ")
        print()
    

def eighth_pattern(number):
    """
            *
          * * *
        * * * * *
      * * * * * * *
    * * * * * * * * * 
    * * * * * * * * * 
      * * * * * * *
        * * * * * 
          * * * 
            *
    """
    fifth_pattern(number)
    seventh_pattern(number)


print('---- Pattern Starts ----')
first_pattern(5)
fifth_pattern(5)
second_pattern(5)
third_pattern(5)
sixth_pattern(5)
fourth_pattern(5)
seventh_pattern(5)
eighth_pattern(5)
print('---- Pattern Ends ----')


"""Manual Slicing"""
# def slice_it(array, start, stop, step):
#     sliced_array = []
#     for i in range(start, stop, step):
#         sliced_array.append (array[i])
#     return sliced_array


# # Test Case 0 
# arr = [5, 4, 3, 2, 1]
# start, stop, step = 0, len(arr), 1
# expected = [5, 4, 3, 2, 1]
# actual = slice_it(arr, start, stop, step)
# isEqual(expected, actual)


# # Test Case 1
# arr = [5, 4, 3, 2, 1]
# start, stop, step = 0, 1, 1
# expected = [5]
# actual = slice_it(arr, start, stop, step)
# isEqual(expected, actual)


"""Array Left Rotation :)"""
# def left_rotate(arr, k):
#     if k == 0:
#         return arr

#     """
#     -> Grab the last k elements store them somewhere
#         # (assuming that the total length is N)
#         # What will be the index of kth element? Ans: (N - 1 - k)
#         # What will be the index of the last element? Ans: (N - 1)
        
#         # Can you now get the values of last k items?

#     -> Append the rest of the array
#     """
#     N = len(arr)
#     k = k % N
#     first_segment = []

#     for i in range((N - k), N, 1):
#         first_segment.append(arr[i])

#     second_segment = []
#     for i in range(N-k):
#         second_segment.append(arr[i])
    
#     return first_segment + second_segment
    


# # Test Case 0
# arr = [1, 2, 3, 4, 5]
# k = 0
# expected = [1, 2, 3, 4, 5]
# actual = left_rotate(arr, k)
# isEqual(expected, actual)



# # Test Case 1
# arr = [1, 2, 3, 4, 5]
# k = 1
# expected = [5, 1, 2, 3, 4]
# actual = left_rotate(arr, k)
# isEqual(expected, actual)



# # Test Case 2
# arr = [1, 2, 3, 4, 5]
# k = 2
# expected = [4, 5, 1, 2, 3]
# actual = left_rotate(arr, k)
# isEqual(expected, actual)



# # Test Case 3
# arr = [1, 2, 3, 4, 5]
# k = 5
# expected = [1, 2, 3, 4, 5]
# actual = left_rotate(arr, k)
# isEqual(expected, actual)


# # Test Case 4
# arr = [1, 2, 3, 4, 5]
# k = 6
# expected = [5, 1, 2, 3, 4]
# actual = left_rotate(arr, k)
# isEqual(expected, actual)




"""# def fibonacci(number):"""
#     x = 0
#     y = 1
#     print(x)
#     print(y)
#     for i in range(number):
#         z=x+y
#         x=y
#         y=z
#         print(z)


# fib(n) = fib(n - 1) + fib(n - 2)

# recursion Tree


"""
number = 3

return fib(3 - 1) + fib(3 - 2)
=> return fib(2) + fib(1)


-------
fib(2) => return fib(1) + fib(0)

fib(1) => 1
"""


"""# def fibonacci_recursion(number):"""
#     # base case || guard case || termination Condition
#     if number == 0:
#         return 0
    
#     if number == 1:
#         return 1

#     return fibonacci_recursion(number - 1) + fibonacci_recursion(number - 2)


# for i in range(8):
#     print(fibonacci_recursion(i))


# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...

# fibonacci(5)
# # Test Case 1
# upto = 0
# expected = []
# actual = fibonacci(upto)
# isEqual(expected, actual)



"""# OOP => Object Oriented Programming

# INHERITANCE

# PARENT CLASS => BASE/SUPER?
# CHILD CLASS => DERIVED

# Exception => Parent CLASS
#   |
# ArithmaticException
#   |
"""

# Recursion 

# class FactorialDoesNotExists(Exception):
#     pass


# def factorial(number):
#     if number == 0:
#         return 1

#     if number < 0:
#        raise FactorialDoesNotExists
    
#     return number * factorial(number - 1)


# # Test Case 1
# number = 0
# expected = 1
# actual = factorial(number)
# isEqual(expected, actual)


# # Test Case 2
# number = -1
# try:
#     actual = factorial(number)
#     print('FAILED')
# except FactorialDoesNotExists:
#     print('PASSED')


# # Test Case 3
# number = 5
# expected = 5 * 4 * 3 * 2 * 1
# actual = factorial(number)
# isEqual(expected, actual)

# for i in range(1,11):
#     print(i)
# 
# i=1
# while(i<11):
#     print(i)
#     i=i+1
    



"""----- ANAGRAM -----"""
# def is_anagram(first_string, second_string):
#     # - check the both string length
#     # - find the character_frequency_map of  string1
#     # - find the character_frequency_map of  string2
#     # - Compare the character_frequency_map of both strings
#     # - return the is_anagram
    
#     first_string_length = len(first_string) 
#     second_string_length = len(second_string) 
    
#     if first_string_length != second_string_length: 
#         return False
        
#     frequency_map_of_first_string = get_character_frequency_map(first_string) 
#     frequency_map_of_second_string = get_character_frequency_map(second_string)

#     return frequency_map_of_first_string == frequency_map_of_second_string 


"""# def get_character_frequency_map(string):"""
#     # - define blank dictionery
#     # - change the string into set
#     # Repeat for each item in the set:
#     #   - count the occurrence of the character in the given string
#     #   - update the dictionery
#     # - return dictionery to caller function
    
#     hashmap = {}
#     unique_characters = set(string)

#     for unique_character in unique_characters:  
#         count = 0

#         for character in string: 
#             if character == unique_character:
#                 count= count+1
        
#         hashmap[unique_character] = count 
   
#     return hashmap

# # Test Case 1
# first_string = 'ABCAD'
# second_string = 'DAABC'
# expected = True
# actual = is_anagram(first_string, second_string)
# isEqual(expected, actual)

# # Test Case 2
# first_string = 'ABZZAD'
# second_string = 'DAABCA'
# expected = False
# actual = is_anagram(first_string, second_string)
# isEqual(expected, actual)

# # Test Case 3
# first_string = 'ABZZ'
# second_string = 'DAABCA'
# expected = False
# actual = is_anagram(first_string, second_string)
# isEqual(expected, actual)

# # Test Case 4
# first_string = 'BAAAB'
# second_string = 'ABBBA'
# expected = False
# actual = is_anagram(first_string, second_string)
# isEqual(expected, actual)


"""Week 2 | Day 1.5"""

# def sum_of_digits(num):
#     str_number = str(num)
#     total = 0
#     for digit in str_number:
#         total = total + int(digit)
#     return total

"""def sum_of_digits(num):"""
#     # Can you break the number into digits?
#     # Decimal Number? Octal? Binary? -> Decimal
#     # What is the Base of the Number? -> 10
#     # What happens when you divide A Number by the Base?
#     # What are the outputs of a division operation? Can they help you somehow?
    
#     # 1234 / 10 = 123, 4 
#     # 123  / 10 = 12 , 3
#     # 12   / 10 = 1  , 2
#     # 1    / 10 = 0  , 1
    
#     # Set accumulated_sum = 0
#     # Repeat UNTIL quotient is 0
#         # divide the number by 10
#         # Add the remainder to accumulated_sum
#         # Store the quotient as the new number
#     # Return the accumulated_sum
#     accumulated_sum = 0
#     digits = 0
#     while (num > 0):
#         digits = num % 10
#         num = num // 10
#         accumulated_sum = accumulated_sum + digits
#     return accumulated_sum


# number = 1234
# expected = 10
# actual = sum_of_digits(number)
# isEqual(expected, actual)


# number = 13221
# expected = 9
# actual = sum_of_digits(number)
# isEqual(expected, actual)



"""# def is_palindrome(num):"""
#     string_number = str(num)
#     reverse_string_number = string_number[::-1]
#     return string_number == reverse_string_number


# def is_palindrome(num):
#     string_number = str(num)
#     total_length = len(string_number)
#     for i in range(total_length):
#         if string_number[i] != string_number[total_length - i - 1]:
#             return False
#     return True
    

# number = 12221
# expected = True
# actual = is_palindrome(number)
# isEqual(expected, actual)


# number = 13221
# expected = False
# actual = is_palindrome(number)
# isEqual(expected, actual)


# 5 + 2 = 7
# 5 - 2 = 3
# 5 * 2 = 10
# 5 / 2 = 2.5
# 5 // 2 = 2
# 5 % 2 = 1

# # 1 2 3 4
# arr = list(map(int, input().split(' ')))

# name = input()
# age = int(input())
# money = float(input())

# # Lookup is O(N)
# arr = []
# length_of _arr = len(arr)

# range(start,stop,step)

# for i in range(len(arr)):
#     pass


# for i in iterable:
#     pass

# # Lookup is O(1)
# hashmap = {
#     'name':'ashwin'
# }
# hashmap[key] = value



"""------------------------------------ Day 5 ------------------------------------"""
"""def get_the_number_of_pairs_that_adds_upto(target, array):"""
    # count = 0
    # array_dict = {}

    # for value in array:
    #     array_dict[value] = 'Put Anything Here...'
    
    # for value in array:
    #     second_element = target - value
    #     if second_element in array_dict:
    #         count = count + 1
      
    # return count // 2


"""def get_the_number_of_pairs_that_adds_upto(target, array):"""
    # count = 0

    # for value in array:
    #     second_element = target - value
    #     if second_element in array:
    #         count = count + 1
      
    # return count // 2


"""def get_the_number_of_pairs_that_adds_upto(target, array):"""
#     count = 0
#     for i in range(len(array)):
#         for j in range(i+1, len(array)):
#             value = array[i] + array[j] 
#             if value == target:
#                 count = count + 1
#     return count


# arr = [1, 2, 3, 4, 5, 6]
# target_sum = 9

# expected = 2
# unordered_pairs = get_the_number_of_pairs_that_adds_upto(target_sum, arr)

# print('PASSED' if expected == unordered_pairs else 'FAILED') 



"""------------------------------------ Day 4 ------------------------------------"""

"""def filter_duplicates_fasttoo_fasttoo(array):"""
#     unique_dict = {}
#     unique_values = []

#     for element in array:
#         if element not in unique_dict:
#             unique_values.append(element)
#             unique_dict[element] = True
            
#     return unique_values


# arr = [1, 1, 1, 1, 1, 1, 2, 3, 5, 3, 4, 2]
# expected = [1, 2, 3, 5, 4]
# unique_value_array = filter_duplicates_fasttoo_fasttoo(arr)
# print('PASSED' if expected == unique_value_array else 'FAILED') 



"""
----------------------
| Sorting Techniques |
----------------------

1. Counting Sort:
-------------------
> Radix sort

2. Hybrid Sort:
-------------------
> Tim sort

3. Comparison Sort:
-------------------
> Bubble Sort     (T) - Worst Case: O(n^2)    | Average Case: O(n^2)      | Best Case: O(n)
> Selection Sort  (T) - Worst Case: O(n^2)    | Average Case: O(n^2)      | Best Case: O(n^2)
> Quick Sort      (T) - Worst Case: O(n^2)    | Average Case: O(NlogN)    | Best Case: O(NlogN)
> Merge Sort      (T) - Worst Case: O(NlogN)  | Average Case: O(NlogN)    | Best Case: O(NlogN)
"""




"""def find_common_elements(first_array, second_array):"""
#     second_array_map = {}

#     for element in second_array:
#         second_array_map[element] = True
    
#     common_items = []
#     for element in first_array:
#         if element in second_array_map:
#             common_items.append(element)
#     return common_items


# arr = [5,6,7,8,9]
# arr2 = [9,10,11,12,13,14,15]

# common_elements = find_common_elements(arr, arr2)
# expected= [ 9 ]

# print('PASSED' if expected == common_elements else 'FAILED') 




"""def find_common_elements(first_array, second_array):"""
#     common_items = []
#     for element in first_array:
#         if element in second_array:
#             common_items.append(element)
#     return common_items



# arr = [5,6,7,8,9]
# arr2 = [9,10,11,12,13,14,15]

# common_elements = find_common_elements(arr, arr2)
# expected= [ 9 ]

# print('PASSED' if expected == common_elements else 'FAILED') 


"""------------------------------------ Day 3 ------------------------------------"""
# Take a int array as Input, space separated
# arr = list(map(int, input().split(' ')))



"""# def find(array, elem):"""
#     for i in range(len(array)):
#         if array[i] == elem:
#             return True
#     return False 

# arr = [1, 2, 3, 4, 5, 6]
# elem_to_be_finded = 3
# expected = True

# is_found = find(arr, elem_to_be_finded)

# print(is_found)
# print('PASSED' if expected == is_found else 'FAILED') 



"""# def filter_duplicates(array):"""
#     unique_values = []

#     for value in array:
#         if value not in unique_values:
#             unique_values.append(value)

#     return unique_values


# arr = [1, 1, 1, 1, 1, 1, 2, 3, 5, 3, 4, 2]
# expected = [1, 2, 3, 5, 4]

# unique_value_array = filter_duplicates(arr)

# print(unique_value_array)
# print('PASSED' if expected == unique_value_array else 'FAILED') 



"""# def find_kth_last_element(array, k):"""
#     return array[len(array) - 1 - k]

# arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# k = 3
# ans = 6

# kth_last_element = find_kth_last_element(arr, k)
# print(kth_last_element, ans == kth_last_element) 



"""# def find_middle_element(array):"""
#     mid = len(array) // 2
#     return array[mid]

# mid_element = find_middle_element(arr)
# print(mid_element) 



"""# Reverse the list & store it a a new list without slicing and no array methods."""
# def rev(array):
#     temp = []
#     for i in range(len(array)-1,-1,-1):
#         temp.append(array[i])
#     return temp

# rev_arr = rev(arr)
# print(rev_arr) # [4,3,2,1]



"""# Print each elem in a new line, in reverse order..."""
# for i in range(len(arr) - 1, -1, -1):
#     print(arr[i])



"""# Print each elem in a new line."""
# for i in range(len(arr)):
#     print (arr[i])



"""------------------------------------ Day 2 ------------------------------------"""
# splitted_string_as_list = input_string.split(',')
# arr = []
# print(splitted_string_as_list)
# for value in splitted_string_as_list:
#     arr.append(int(value))
# print(arr)


"""# Take Integer Input"""
# number = int(input("enter"))

# prime number check...
# is_prime = True

# for i in range(2, number):
#     if number % i == 0:
#         is_prime = False
#         break

# if is_prime:
#     print("prime")
# else:
#     print("NOt prime")


#if Prime == True:
    # print("Prime")
#else:
    # 

"""# Foo-Bar-Baz"""
# 1. multiple of 3 => FOO
# 2. multiple of 5 => Bar
# 3. multiple of 3 & multiple of 5 => Baz
# for i in range(0, number+1):
    # if i == 0:
    #     print(i)

    # elif i % 3 == 0 and i % 5 == 0: 
    #     print(i, "Baz")

    # elif i % 5 == 0:
    #     print(i, "Bar")

    # elif i % 3 == 0:
    #     print(i, "FOO")
        
    # else:
    #     print(i)



# for i in range(0,number+1):
#     print(i)

# for i in range(number, -1, -1):
#     print(i)



# if number % 2 == 0:
#     print("number is even")
# else:
#     print("number is odd")

# if number  ==  5:
#     print("number is 5")

# elif number == 3:
#     print("number is 3")
    
# else:
#     print("modulo ", number % 4)



"""# Palindrome Check..."""
#paliandrome = a word, phrase, or sequence that reads the same backwards as forwards.
#FIRST APPROACH
# reverse_string = str_input[::-1]
# if str_input == reverse_string:
#     print('This word is paliandrome')
# else:
#     print('This is not a paliandrome')
# print(reverse_string, str_input)


# SECOND APPROACH
# def length_of_given_string(string):
#     count_the_string=0
#     for character in string:
#         count_the_string = count_the_string + 1
#     return count_the_string

# # access the elements using indexing
# reverse_string = ''
# length_of_string = length_of_given_string(str_input)-1
# while length_of_string >= 0:
#     reverse_string = reverse_string + str_input[length_of_string]
#     length_of_string = length_of_string - 1
# print(reverse_string)

# if str_input == reverse_string:
#     print('It Is a Paliandrome')
# else:
#     print('It is Not a paliandrome')

"""# Take a String as a Input & store it """
# s = input("Enter the string: ")


"""------------------------------------ Day 1 ------------------------------------"""
"""# count the occurrences of every distinct character"""
# haaallo
# h: 1
# a: 3
# l: 2
# o: 1
# frequency = {}

# for character in s:
#     if character in frequency:
#         frequency[character] += 1
#     else:
#         frequency[character] = 1

# for key in frequency:
#     print(key, frequency[key])



# distinct_characters = set(s)
# for character in distinct_characters:
#     count = 0
#     for character_new in s:
#         if character == character_new:
#             count = count + 1
#     print(character, count)



"""# count the number of vowels & consonants together"""
# vowels = ['a','e','i','o','u']
# consonant_count, vowel_count = 0, 0
# for character in s:
#     if not character.isalpha():
#         continue

#     if character.lower() in vowels:
#         vowel_count = vowel_count + 1
#         continue
    
#     consonant_count = consonant_count + 1
# print(consonant_count, vowel_count)



"""# count the number of vowels & consonants together"""
# vowels = ['a','e','i','o','u']
# consonant_count = 0
# vowel_count = 0
# for character in s:
#     if character.isalpha() and character.lower() not in vowels:
#         consonant_count = consonant_count + 1
        
#     elif character.isalpha() and character.lower() in vowels:
#         vowel_count = vowel_count + 1
    
# print(consonant_count)
# print(vowel_count)



"""# count the number of consonants"""
# vowels = ['a','e','i','o','u']
# count = 0
# for character in s:
#     if character.isalpha() and character.lower() not in vowels:
#         count = count + 1
# print(count)



"""# count the number of vowels"""
# vowels = ['a','e','i','o','u']
# count = 0
# for character in s:
#     if character in vowels:
#         count = count + 1
# print(count)



"""# count the occurance of 'a' in S"""
# count_of_a = 0
# for character in s:
#     if character == 'a':
#         count_of_a = count_of_a + 1
# print(count_of_a)



"""# Count the number of Characters."""
# print(len(s))
# count = 0
# for length in s:
#     count = count + 1
# print(count)



"""# Print Each Character in the String on Different Lines."""
# for each_character in string:
    # print(each_character)



# & then print it
# print(string)
