'''
Exercise 3:
    Write a program to read through a mail log, build a histogram using a\
        dictionary to count how many messages have come from each email
        address, and print the dictionary.

    Sample Line:
        From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008

    ----Example:
        Enter file name: mbox-short.txt
        {'gopal.ramasammycook@gmail.com': 1, 'louis@media.berkeley.edu': 3,
        'cwen@iupui.edu': 5, 'antranig@caret.cam.ac.uk': 1,
        'rjlowe@iupui.edu': 2, 'gsilver@umich.edu': 3,
        'david.horwitz@uct.ac.za': 4, 'wagnermr@iupui.edu': 1,
        'zqian@umich.edu': 4, 'stephen.marquard@uct.ac.za': 2,
        'ray@media.berkeley.edu': 1}
'''

dict_mail = dict()

file_name = input('Enter file name: ')
try:
    file = open(file_name)
except:
    print('File cannot be opened:', file_name)
    exit()

for line in file:
    if(line.startswith("From ")):
        raw_email = line.split(' ')
        email = raw_email[1]
        dict_mail[email] = dict_mail.get(email,0) + 1

print(dict_mail)

