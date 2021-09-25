'''
Exercise 1:
    Download a copy of the file www.py4e.com/code3/words.txt

    Write a program that reads the words in words.txt and stores\
        them as keys in a dictionary. It doesn’t matter what the
        values are. Then you can use the in operator as a fast way
        to check whether a string is in the dictionary.
'''

file_name = input('Enter file name: ')
try:
    file = open(file_name)
except:
    print('File cannot be opened:', file_name)
    exit()

dic = dict()
for line in file:
    line = line.rstrip().split()
    for key in line:
        dic[key] = dic.get(key,0) + 1

print(dic)