"""
Revise a previous program as follows: Read and parse the
“From” lines and pull out the addresses from the line. Count the number of messages from each person using a dictionary.
After all the data has been read, print the person with the most commits
by creating a list of (count, email) tuples from the dictionary. Then
sort the list in reverse order and print out the person who has the most
commits.

Sample Line:
From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008

Enter a file name: mbox-short.txt
cwen@iupui.edu 5
Enter a file name: mbox.txt
zqian@umich.edu 195
"""
file_name = input('Enter a file name: ')
try:
    file_handle = open(file_name, 'r')
    email_counts = dict()
    lst = list()

    for line in file_handle:
        if line.startswith('From '):
            email = line.split()[1]
            email_counts[email] = email_counts.get(email, 0) + 1

    for email, count in email_counts.items():
        lst.append((count, email))
        lst = sorted(lst, reverse = True)

    count, email = lst[0]
    print(email, count)
        
except FileNotFoundError:
    print(f"File '{file_name}' not found.")
    quit()

