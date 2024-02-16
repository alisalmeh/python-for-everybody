"""
Rewrite the guardian code in the above example without
two if statements. Instead, use a compound logical expression using
the or logical operator with a single if statement.
"""
file = open('mbox-short.txt')

for line in file:
    words = line.split()
    if len(words) == 0 or words[0] != 'From' : continue
    print(words[2])