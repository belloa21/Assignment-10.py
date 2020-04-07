# Alex Bello
# 4/7/2020
# The methods for the palindrome program


def palindrome_check(line):
    line = line.lower()
    line = line.strip()
    length = int(len(line))
    if length == 0 or length == 1:
        return True
    elif line[0] != line[-1]:
        return False
    else:
        return palindrome_check(line[1:-1])


def punc_check(line):
    # Declaring what the punctuation marks are
    punctuation_marks = '''!@#$%^&*()-;:'"/?.,><'''
    # Check line for any punctuation marks
    for punc in line.lower():
        # Remove any punctuation marks in the line
        if punc in punctuation_marks:
            line = line.replace(punc, "")
    # Reprint the new line
    print(line)
    # Run new line through palindrome_check to see if its a palindrome
    palindrome_check(line)



