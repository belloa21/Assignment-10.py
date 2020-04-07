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
    for x in line.lower():
        if x in punctuation_marks:
            line = line.replace(x, "")
    # This will reprint the string without the punctuation marks
    print(line)



