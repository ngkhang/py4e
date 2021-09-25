'''
Exercise 2:
    Write a program that categorizes each mail message by which day of the week\
        the commit was done. To do this look for lines that start with “From”,
        then look for the third word and keep a running count of each of the days
        of the week. At the end of the program print out the contents of your
        dictionary (order does not matter).

    Sample Line:
        From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008

    ---- Example:
        python dow.py
        Enter a file name: mbox-short.txt
        {'Fri': 20, 'Thu': 6, 'Sat': 1}
'''

file_name = input('Enter file name: ')
try:
    file = open(file_name)
except:
    print('File cannot be opened:', file_name)
    exit()

day =dict()

for line in file:
    if(line.startswith('From ')):
        words = line.split(' ')
        key = words[2]
        day[key] = day.get(key,0) + 1

print(day)