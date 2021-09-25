'''
Exercise 6:
    Rewrite your pay computation with time-and-a-half for overtime\
        and create a function called computepay which takes two
        parameters (hours and rate).

    ----Example:
        Enter Hours: 45
        Enter Rate: 10
        Pay: 475.0
'''
def computepay(hours, rate):
    if(hours>40):
        pay = (40 + (hours-40)*1.5 )*rate
    else:
        pay = hours*rate
    return print('Pay:', pay)

try:
    hrs = int(input('Enter Hours: '))
    rt = float(input('Enter Rate: '))
except:
    print('Error, please enter numeric input')
    quit()

computepay(hrs,rt)