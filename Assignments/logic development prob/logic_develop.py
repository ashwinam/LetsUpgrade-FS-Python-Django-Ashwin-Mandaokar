'''
Python keyword
int float str
for while
range
return
if elif else
pass break continue
in is
def
not and
yield
from import
try except
lambda filter map
class
True False
None
Global
'''






#str_input=input('enter the string :\n')
#print(str_input)

# 1)print each character
#for each_char in str_input:
    #print(each_char)
    
# 2)count the number of characters.
#print(len(str_input))
'''
count = 0
for each_character in str_input:
    count = count + 1
    
print(count)
'''

# 3) count the occurences of 'a' in s

'''
count_of_char = 0
for character in str_input:
    #if character == 'a':
     #if 'a' in character:
    if character in 'a':
        count_of_char = count_of_char + 1

print(count_of_char)
'''
# 4) count the occurences of vowels.
# first approach
'''
list_of_vowels=['a','e','i','o','u']
counter_for_vowels=0
for vowel_char in str_input:
    if vowel_char in list_of_vowels:
        counter_for_vowels = counter_for_vowels + 1
print(counter_for_vowels)
'''

#second approach
'''
counter_for_vowels=0
counter_for_consonants=0
for vowel_character in str_input:
    if vowel_character == 'a' or vowel_character == 'e' or vowel_character == 'i' or vowel_character == 'o' or vowel_character == 'u':
        counter_for_vowels = counter_for_vowels + 1
    else:
        counter_for_consonants = counter_for_consonants + 1
print(counter_for_vowels)
print(counter_for_consonants)
'''

# 5) count the occurences of consonants.
# first approach
'''
list_of_vowels=['a','e','i','o','u']
counter_for_consonants=0
for vowel_char in str_input:
    if vowel_char not in list_of_vowels:
        counter_for_consonants = counter_for_consonants + 1
print(counter_for_consonants)
'''
# second approach
'''
list_of_vowels=['a','e','i','o','u']
counter_for_consonants=0
for vowel_char in str_input:
    if vowel_char.isalpha() and vowel_char.lower() not in list_of_vowels:
        counter_for_consonants = counter_for_consonants + 1
print(counter_for_consonants)
'''

# 6) count the occurences of consonants and vowels.
# first approach
'''
list_of_vowels=['a','e','i','o','u']
counter_for_consonants=0
counter_for_vowels=0
for vowel_char in str_input:
    if vowel_char.isalpha() and vowel_char.lower() not in list_of_vowels:
        counter_for_consonants = counter_for_consonants + 1
    elif vowel_char.isalpha() and vowel_char.lower() in list_of_vowels:
        counter_for_vowels = counter_for_vowels + 1
print('the total conconants is :' + str(counter_for_consonants))
print('the total vowels is :' + str(counter_for_vowels))
'''

# second approach
'''
list_of_vowels=['a','e','i','o','u']
counter_for_consonants=0
counter_for_vowels=0
for vowel_char in str_input:
    if not vowel_char.isalpha():
        continue
    if vowel_char.lower() in list_of_vowels:
        counter_for_vowels = counter_for_vowels + 1
        
    else:
        counter_for_consonants = counter_for_consonants + 1
print('the total conconants is :' + str(counter_for_consonants))
print('the total vowels is :' + str(counter_for_vowels))
'''

# count the occurrences of every distinct character
# first approach
'''
string_set= set(str_input)
for character in string_set:
    count = 0
    for new_character in str_input:
        if character == new_character:
            count = count + 1
    print(character, count)
'''
# second approach
'''
frequency = {}

for character in str_input:
    if character in frequency:
        frequency[character] += 1
    else:
        frequency[character] = 1

for key in frequency:
    print(key, frequency[key])
'''

'''
Algorithm: 
isPalindrome(str) 
1) Find length of str. Let length be n. 
2) Initialize low and high indexes as 0 and n-1 respectively. 
3) Do following while low index ‘l’ is smaller than high index ‘h’. 
…..a) If str[l] is not same as str[h], then return false. 
…..b) Increment l and decrement h, i.e., do l++ and h–. 
4) If we reach here, it means we didn’t find a mis
Following is C implementation to check if a given string is palindrome or not.
'''



# Write a program to check for the paliandrome
# Paliandrome means = a word, phrase, or sequence that reads the same backwards as forwards,
# requirements:
# > first need to reverse the string.
# > second check the condition both is same or not
#FIRST APPROACH
'''
reverse_string=str_input[::-1]
if str_input == reverse_string:
    print('This word is paliandrome')
else:
    print('This is not a paliandrome')
print(reverse_string, str_input)
'''

# SECOND APPROACH
'''
def length_of_given_string(string):
    count_the_string=0
    for character in string:
        count_the_string = count_the_string + 1
    return count_the_string

# access the elements using indexing
reverse_string = ''
length_of_string = length_of_given_string(str_input)-1
while length_of_string >= 0:
    reverse_string = reverse_string + str_input[length_of_string]
    length_of_string = length_of_string - 1
print(reverse_string)

if str_input == reverse_string:
    print('It Is a Paliandrome')
else:
    print('It is Not a paliandrome')

'''
'''
def reverse_while_loop(s):
    s1 = ''
    length = len(s) - 1
    while length >= 0:
        s1 = s1 + s[length]
        length = length - 1
    return s1

input_str = 'ABç∂EF'

if __name__ == "__main__":
    print('Reverse String using while loop =', reverse_while_loop(input_str))
'''

'''
def reverse_for_loop(s):
    s1 = ''
    for c in s:
        s1 = c + s1  # appending chars in reverse order
    return s1

input_str = 'ABç∂EF'

if __name__ == "__main__":
    print('Reverse String using for loop =', reverse_for_loop(input_str))
'''


a = list(input())
b = list(input())
a.sort(reverse=False)
print(a)
b.sort(reverse=False)
print(b)
if a.sort() == b.sort():
    print('this is a anagram')
else:
    print('not an anagram')
    

