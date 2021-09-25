'''
Exercise 2:
    Write a program to prompt for a file name, and then read through\
        the file and look for lines of the form:
            X-DSPAM-Confidence: 0.8475

    When you encounter a line that starts with “X-DSPAM-Confidence:”\
        pull apart the line to extract the floating-point numberber
        on the line. Count these lines and then compute the total of
        the spam confidence values from these lines. When you reach
        the end of the file, print out the average spam confidence.

    ----Example:
        Enter the file name: mbox.txt
        Average spam confidence: 0.894128046745

        Enter the file name: mbox-short.txt
        Average spam confidence: 0.750718518519

    ----Note:
        Test your file on the mbox.txt and mbox-short.txt files.
'''
count = 0
total = 0
number = 0

file_name = input('Enter the file name: ')
file = open(file_name,'r')

for letter in file:
    letter = letter.rstrip()
    if(letter.startswith('X-DSPAM-Confidence: ')):
        number = float(letter[len('X-DSPAM-Confidence: ') + 1:])
        count += 1
        total += number


aver_confi = total/count
print('There were', count, 'value in', file_name)
print('Total:', total)
print('Average spam confidence:',aver_confi)