'''
Exercise 6:
    Rewrite the program that prompts the user for a list of numbers\
        and prints out the maximum and minimum of the numbers at the
        end when the user enters “done”. Write the program to store
        the numbers the user enters in a list and use the max() and
        min() functions to compute the maximum and minimum numbers
        after the loop completes.

    ----Example:
        Enter a number: 6
        Enter a number: 2
        Enter a number: 9
        Enter a number: 3
        Enter a number: 5
        Enter a number: done
        Maximum: 9.0
        Minimum: 2.0
'''
stop = ''
max_num = 0
min_num = 0
lst=[]

while(stop != 'done'):
    number = input('Enter a number: ')

    try:
        if(number == 'done'):
            stop = 'done'
            break
        number = float(number)
        lst.append(number)
    except:
        print('Invalid input')
        continue

    max_num = max(lst)
    min_num = min(lst)

print('Maximum:', max_num)
print('Minimum:', min_num)
