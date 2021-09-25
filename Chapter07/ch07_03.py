'''
Exercise 3:
    Sometimes when programmers get bored or want to have a bit\
        of fun, they add a harmless Easter Egg to their program.
        Modify the program that prompts the user for the file name
        so that it prints a funny message when the user types in
        the exact file name “na na boo boo”. The program should
        behave normally for all other files which exist and don’t
        exist. Here is a sample execution of the program:

    ----Example:
        python egg.py
        Enter the file name: mbox.txt
        There were 1797 subject lines in mbox.txt

        python egg.py
        Enter the file name: missing.tyxt
        File cannot be opened: missing.tyxt

        python egg.py
        Enter the file name: na na boo boo
        NA NA BOO BOO TO YOU - You have been punk'd!
'''

count = 0
string = 'na na boo boo'
file_name = input('Enter the file name: ')

if(file_name == string):
    print(string.upper() + " TO YOU - You have been punk'd!")
    exit()

try:
    file = open(file_name,'r')
except:
    print('File cannot be opened:', file_name)
    exit()

for letter in file:
    if(letter.startswith('Subject:')):
        count += 1

print('There were', count, 'subject lines in', file_name)
