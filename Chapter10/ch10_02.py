'''
Exercise 2
    This program counts the distribution of the hour of the day for\
        each of the messages. You can pull the hour from the “From”
        line by finding the time string and then splitting that
        string into parts using the colon character. Once you have
        accumulated the counts for each hour, print out the counts,
        one per line, sorted by hour as shown below.

    Sample Line:
        From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008

    ----Example:
        Enter a file name: mbox-short.txt
        04 3
        06 1
        07 1
        09 2
        10 3
        11 6
        14 1
        15 2
        16 4
        17 2
        18 1
        19 1
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
        raw = line.split()
        raw_time = raw[5].split(':')
        hour = raw_time[0]
        dic[hour] = dic.get(hour,0) +1

lst = list()
for hr, count in dic.items():
    lst.append((hr, count))

lst.sort(reverse=False)

for hr, count in lst:
    print(hr, count)

# for i in range(0,len(lst)):
#     tup = lst[i]
#     print(tup[0], tup[1])

