"""
Encapsulate this code in a function named count, 
and generalize it so that it accepts the string and the letter as arguments.
"""
def count(word, letter):
    count = 0
    for character in word:
        if character == letter:
            count += 1
    return count

word = input('Enter a string: ')
character = input('Enter the letter: ')
print('Count', count(word, character))