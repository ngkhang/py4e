'''
Exercise 1:
    Write a simple program to simulate the operation of the grep command\
        on Unix. Ask the user to enter a regular expression and count the
        number of lines that matched the regular expression:
            $ python grep.py
            Enter a regular expression: ^Author
            mbox.txt had 1798 lines that matched ^Author

            $ python grep.py
            Enter a regular expression: ^X-
            mbox.txt had 14368 lines that matched ^X-

            $ python grep.py
            Enter a regular expression: java$
            mbox.txt had 4175 lines that matched java$
'''
import re
count = 0

# Read a file
file_name = input('Enter a file name: ')
regular = input('Enter a regular expression: ')

try:
    file = open(file_name)
except:
    print('File cannot be opened: ', file_name)
    quit()

for line in file:
    line = line.rstrip()
    find = re.findall(regular,line)
    if (len(find) > 0):
        count += 1
print('{} had {} lines that matched {}'.format(file_name, count, regular))