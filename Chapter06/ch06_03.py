'''
Exercise 3:
    Encapsulate this code in a function named count, and generalize\
        it so that it accepts the string and the letter as arguments.

    ----Example:
        word = 'banana'
        count = 0
        for letter in word:
        if letter == 'a':
        count = count + 1
        print(count)
'''
def count(str_1, str_sub):
    count_num = 0
    for letter in str_1:
        if letter == str_sub:
            count_num = count_num + 1
    print(count_num)

word = input('Input a word: ')
letter = input('Input a letter: ')
count(word, letter)