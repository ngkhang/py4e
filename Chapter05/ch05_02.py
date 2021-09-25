'''
Exercise 2:
    Write another program that prompts for a list of numbers as\
        above and at the end prints out both the maximum and
        minimum of the numbers instead of the average.
'''

total = 0
count = 0
max_num = None
min_num = None

while(True):
    num = input('Enter a number: ')
    if(num == 'done'):
        break
    try:
        num = int(num)
    except:
        print('Invalid input')
        continue
    count += 1
    total += num

    if(max_num == None or max_num < num):
        max_num = num
    if(min_num == None or min_num > num):
        min_num = num

print(total, count, max_num, min_num)