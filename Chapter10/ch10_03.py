'''
Exercise
    Write a program that reads a file and prints the letters in decreasing order of frequency.\
        Your program should convert all the input to lower case and only count the letters a-z.
        Your program should not count spaces, digits, punctuation, or anything other than the
        letters a-z. Find text samples from several different languages and see how letter
        frequency varies between languages.

    Compare your results with the tables at https://wikipedia.org/wiki/Letter_frequencies.
'''
# Read a file
file_name = input('Enter a file name: ')
try:
    file = open(file_name)
except:
    print('File cannot be opened:', file_name)
    quit()

# Created a Dictionary for Alphabet
alphabet = 'abcdefghijklmnopqrstuvwxyz'
dict_alpha = dict()
for i in range(0,len(alphabet)):
    char_temp = alphabet[i]
    dict_alpha[char_temp] = 0

# Read and count all characters in the file
sum_char = 0
list_raw = list()
for line in file:
    line = line.rstrip().lower()
    for text in line:
        if(text in alphabet):
            list_raw.append(text)
            sum_char += 1

# Count characters and add them into Dictionary
for letter in dict_alpha:
    for i in list_raw:
        if(letter == i):
            dict_alpha[letter] = dict_alpha.get(letter,0)+1

# Convert to a list of tuples
# Sort the dictionary by value
list_char = list()
for key,count in dict_alpha.items():
    per = (float(count)/sum_char)
    list_char.append((key, count, per))
list_char.sort(reverse=False)

# Print
print('+ {:-<6} + {:-^5} + {:->7} +'.format('','',''))
print('| {:<3} | {:^3} | {:>7} |'.format('Letter','Count','Percent'))

for key, val, per in list_char:
    key = key.upper()
    print('| {:^6} | {:^5} | {:>7.3%} |'.format(key,val,per))

print('+ {:-<6} + {:-^5} + {:->7} +'.format('','',''))
