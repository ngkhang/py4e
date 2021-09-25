'''
Exercise 1:
    Revise a previous program as follows: Read and parse the “From”\
        lines and pull out the addresses from the line. Count the
        number of messages from each person using a dictionary.

    After all the data has been read, print the person with the most\
        commits by creating a list of (count, email) tuples from the
        dictionary. Then sort the list in reverse order and print out
        the person who has the most commits.

    Sample Line:
        From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008

    ----Example:
        Enter a file name: mbox-short.txt
        cwen@iupui.edu 5
        Enter a file name: mbox.txt
        zqian@umich.edu 195
'''
file_name = input('Enter a file name: ')
try:
    file = open(file_name)
except:
    print('File cannot be opened:', file_name)
    quit()

dic = dict()
for line in file:
    if(line.startswith('From ')):
        raw_str = line.split()
        addr = raw_str[1]
        dic[addr] = dic.get(addr,0) +1

lst = list()
for key, val in dic.items():
    lst.append((val, key))

lst.sort(reverse=True)
person = lst[0]

print(person[1], person[0])