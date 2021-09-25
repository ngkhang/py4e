'''
Exercise 4:
    Add code to the above program to figure out who has the most messages\
        in the file. After all the data has been read and the dictionary
        has been created, look through the dictionary using a maximum loop
        (see Chapter 5: Maximum and minimum loops) to find who has the most
        messages and print how many messages the person has.

    Sample Line:
        From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008

    ----Example:
        Enter a file name: mbox-short.txt
        cwen@iupui.edu 5
        Enter a file name: mbox.txt
        zqian@umich.edu 195
'''

dict_mail = dict()

file_name = input("Enter a file name: ")

try:
    file = open(file_name)
except:
    print("File cannot be opened:", file_name)
    exit()

for line in file:
    if(line.startswith('From ')):
        raw_email = line.split(' ')
        email = raw_email[1]
        dict_mail[email] = dict_mail.get(email,0) + 1

lst_value = list(dict_mail.values())
max_email = max(lst_value)
min_email = min(lst_value)


print('---The most messages')
for i in dict_mail:
    if(dict_mail[i] == max_email):
        print(i, dict_mail[i])

print('\n---At least messages')
for i in dict_mail:
    if(dict_mail[i] == min_email):
        print(i, dict_mail[i])
