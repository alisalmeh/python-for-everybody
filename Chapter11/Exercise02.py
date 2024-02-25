"""
Write a program to look for lines of the form:
New Revision: 39772
Extract the number from each of the lines using a regular expression
and the findall() method. Compute the average of the numbers and
print out the average as an integer.

Enter file:mbox.txt
38549

Enter file:mbox-short.txt
39756
"""
import re
fname = input('Enter file: ')

try:
    fhand = open(fname, 'r')
    
    numbers = list()
    for line in fhand:
        line = line.rstrip()
        match = re.findall('New\sRevision:\s([0-9]+)', line)
        if match:
            numbers.append(int(match[0]))

    average = sum(numbers)/len(numbers)
    print(round(average, 7))
            
except FileNotFoundError:
    print(f"File '{fname}' not found.")
    quit()