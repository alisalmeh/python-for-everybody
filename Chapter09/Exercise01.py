"""
Write a program that reads the words in words.txt and stores them as
keys in a dictionary. It doesn’t matter what the values are. Then you
can use the in operator as a fast way to check whether a string is in the
dictionary.
"""
def create_word_dictionary(file_path):
    word_dictionary = {}
    handle_file = open(file_path, 'r')
        
    for line in handle_file:
        words = line.split()
        for word in words:
            word_dictionary[word] = word_dictionary.get(word, 0) 
        
    return word_dictionary

file_path = 'words.txt'
word_dict = create_word_dictionary(file_path)

search_word = input('Enter the search word: ')

if search_word in word_dict:
    print(f'{search_word} is in the dictionary!')
else:
    print(f'{search_word} is not in the dictionary.')