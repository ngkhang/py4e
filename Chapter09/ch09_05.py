'''
Exercise 5:
    This program records the domain name (instead of the address)\
        where the message was sent from instead of who the mail
        came from (i.e., the whole email address). At the end of
        the program, print out the contents of your dictionary.

    Sample Line:
        From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008

    ----Example:
        python schoolcount.py
        Enter a file name: mbox-short.txt
        {'media.berkeley.edu': 4, 'uct.ac.za': 6, 'umich.edu': 7,
        'gmail.com': 1, 'caret.cam.ac.uk': 1, 'iupui.edu': 8}
'''

dic = dict()

file_name = input("Enter a file name: ")
try:
    file = open(file_name)
except:
    print("File cannot be opened:", file_name)
    exit()

for line in file:
    if(line.startswith("From ")):
        raw = line.split("@")
        raw = raw[1].split(" ")
        domain = raw[0]
        dic[domain] = dic.get(domain, 0) + 1

print(dic)

