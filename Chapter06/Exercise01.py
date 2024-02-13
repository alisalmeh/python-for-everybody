"""
Write a while loop that starts at the last character in the
string and works its way backwards to the first character in the string,
printing each letter on a separate line, except backwards.
"""
fruit = 'banana'
length = len(fruit)
index = length - 1

while index >= 0:
    letter = fruit[index]
    print(index, letter)
    index -= 1