'''
Exercise 4:
    Download a copy of the file www.py4e.com/code3/romeo.txt.\
        Create a list of unique words, which will contain the
        final result. Write a program to open the file romeo.txt
        and read it line by line. For each line, split the line
        into a list of words using the split function. For each
        word, check to see if the word is already in the list of
        unique words.

    If the word is not in the list of unique words, add it to the\
        list. When the program completes, sort and print the list
        of unique words in alphabetical order.

    ----Example:
        Enter file: romeo.txt
        ['Arise', 'But', 'It', 'Juliet', 'Who', 'already',
        'and', 'breaks', 'east', 'envious', 'fair', 'grief',
        'is', 'kill', 'light', 'moon', 'pale', 'sick', 'soft',
        'sun', 'the', 'through', 'what', 'window',
        'with', 'yonder']
'''
word = []

file_name = input('Enter file: ')
file = open(file_name, 'r')

for line in file:
    for text in line.split():
        if(text not in word):
            word.append(text)

word.sort()
print(word)
