"""
Exercise 1:
    Write a function called chop that takes a list and modifies it,\
        removing the first and last elements, and returns None. Then
        write a function called middle that takes a list and returns
        a new list that contains all but the first and last elements.
"""

def chot(lst):
    lst1 = lst.copy()
    lst1.pop(0)
    lst1.pop()
    return None

def middle(lst):
    lst2 = lst.copy()
    lst2.pop(0)
    lst2.pop()
    return print(lst2)

list_1 = [1,2,'abx', [1, 'a'], 'y',3]
chot(list_1)
middle(list_1)