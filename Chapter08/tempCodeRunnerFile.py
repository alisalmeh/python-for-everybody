file_handle:
    words = line.rstrip().split()
    unique_words = list()
    if words in unique_words : continue
    unique_words.append(words)
    print(unique_words)

