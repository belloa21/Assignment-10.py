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


def punccheck(line):
    # Declaring what the punctuation marks are
    punctuation_marks = '''!@#$%^&*()-;:'"/?.,><'''
    for a in line.lower():
        if a in punctuation_marks:
            line = line.replace()
    # This will reprint the string without the punctuation marks
            if line == 0 or 1:
                print(line)




