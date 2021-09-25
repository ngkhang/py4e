'''
Exercise 1:
    Rewrite your pay computation to give the employee 1.5 times\
        the hourly rate for hours worked above 40 hours.

    ----Example:
        Enter Hours: 45
        Enter Rate: 10
        Pay: 475.0

    Note: (40*10 + 5*10*1.5 = 475.0)

'''
hours = int(input('Enter Hours: '))
rate = float(input('Enter Rate: '))

if(hours>40):
    pay = (40 + (hours-40) * 1.5) * rate
else:
    pay = 40 * rate
print('Pay:', pay)
