"""
Write a program that reads a file and prints the letters
in decreasing order of frequency. Your program should convert all the
input to lower case and only count the letters a-z. Your program should
not count spaces, digits, punctuation, or anything other than the letters
a-z. Find text samples from several different languages and see how
letter frequency varies between languages.
"""
file_name = input('Enter a file name: ')
try:
    file_handle = open(file_name, 'r')
    alphabet = ('abcdefghijklmnopqrstuvwxyz')
    text = file_handle.read()
    characters = dict()

    for character in text.lower():
        if character in alphabet:
            characters[character] = characters.get(character, 0) + 1
        
    char_list = list()
    for key, value in characters.items():
        char_list.append((value, key))
    char_list.sort(reverse = True)

    for freq, char in char_list:
        print(char, freq)

except FileNotFoundError:
    print(f"File '{file_name}' not found.")
    quit()