'''
Exercise 2:
    Write a program to look for lines of the form:\
        New Revision: 39772

    Extract the number from each of the lines using a\
        regular expression and the findall() method.
        Compute the average of the numbers and print
        out the average as an integer.

    ----Example:
        Enter file:mbox.txt
        38549

        Enter file:mbox-short.txt
        39756
'''
import re
count = 0
total = 0

# Read a file
file_name = input('Enter a file name: ')
try:
    file = open(file_name)
except:
    print('File cannot be opened: ', file_name)
    quit()

for line in file:
    line = line.rstrip()
    find_line = re.findall('^N.*: ([0-9.]+)',line)
    if(len(find_line) > 0):
        number = find_line[0]
        count += 1
        total += int(number)

average = int(total/count)
print(average)