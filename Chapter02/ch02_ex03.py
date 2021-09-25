'''
Exercise 3:
    Write a program to prompt the user for hours and\
        rate per hour to compute gross pay.

    ----Example:
        Enter Hours: 35
        Enter Rate: 2.75
        Pay: 96.25
'''

# This first line is provided for you

hours = int(input("Enter hours: "))
rate = float(input("Enter rate: "))
pay = hours * rate
print("Pay:", pay)