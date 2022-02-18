import string
s = set(input("Enter the string: ").lower())
alpha = set(string.ascii_lowercase)
print(alpha)
print(s)
if s >= alpha:
  print('Pangram')
else:
  print("Not pangram")
