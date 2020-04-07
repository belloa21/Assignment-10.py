# Alex Bello
# 4/7/2020
# The driver program for seeing if a user input a palindrome
from Methods import palindrome_check
from Methods import punccheck


print("Please enter what you think is a palindrome.")
line = input()
punccheck(line)

if palindrome_check(line):
    print("You got it! That's a palindrome.")
else:
    print("Sorry, that's not a palindrome.")
