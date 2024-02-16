"""
Write a function called chop that takes a list and modifies
it, removing the first and last elements, and returns None. Then write
a function called middle that takes a list and returns a new list that
contains all but the first and last elements.
"""
def chop(t):
    del t[0]
    del t[-1]

fruits = ['banana', 'orange', 'mandarin', 'pomegranate', 'plum']
print(f'chop function: {chop(fruits)}')
print(fruits)

def middle(t):
    return t[1:-1]

fruits = ['banana', 'orange', 'mandarin', 'pomegranate', 'plum']
print(f'middle function: {middle(fruits)}')
print(fruits)   