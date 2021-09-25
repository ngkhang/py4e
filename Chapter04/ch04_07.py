'''
Exercise 7:
    Rewrite the grade program from the previous chapter using\
        a function called computegrade that takes a score as
        its parameter and returns a grade as a string.

            Score     Grade
            >= 0.9       A
            >= 0.8       B
            >= 0.7       C
            >= 0.6       D
            < 0.6        F

    ----Example:
        Enter score: 0.95
        A

        Enter score: perfect
        Bad score

        Enter score: 10.0
        Bad score
'''

def computegrade(score):
    if(score > 1 or score < 0):
        print('Bad score')
    elif (score >= 0.9):
        print('A')
    elif (score >= 0.8):
        print('B')
    elif (score >= 0.7):
        print('C')
    elif (score >= 0.6):
        print('D')
    else:
        print('F')

try:
    score = float(input('Enter score: '))
except:
    print('Bad score')
    quit()

computegrade(score)