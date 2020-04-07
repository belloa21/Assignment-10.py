# Alex Bello
# 4/7/2020
# The driver program for seeing if a user input a palindrome
from Methods import palindrome_check
from Methods import punc_check


print("Please enter what you think is a palindrome.")
line = input()

if palindrome_check(line):
    print("You got it! That's a palindrome.")
else:
    print("Not quite one let's see if we can fix it.")
    punc_check(line)
    print("All fixed up!")

