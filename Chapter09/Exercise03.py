"""
Write a program to read through a mail log, build a histogram using
a dictionary to count how many messages have come from
each email address, and print the dictionary.

Enter file name: mbox-short.txt
{'gopal.ramasammycook@gmail.com': 1, 'louis@media.berkeley.edu': 3,
'cwen@iupui.edu': 5, 'antranig@caret.cam.ac.uk': 1,
'rjlowe@iupui.edu': 2, 'gsilver@umich.edu': 3,
'david.horwitz@uct.ac.za': 4, 'wagnermr@iupui.edu': 1,
'zqian@umich.edu': 4, 'stephen.marquard@uct.ac.za': 2,
'ray@media.berkeley.edu': 1}
"""
def count_messages_from_each_sender(file_name):
    try:
        file_handle = open(file_name, 'r')
        email_addresses = {}

        for line in file_handle:
            if line.startswith('From '):
                words = line.split()
                email = words[1]
                email_addresses[email] = email_addresses.get(email, 0) + 1

        print(email_addresses)
    
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
        quit()

file_path = input('Enter file name: ')
count_messages_from_each_sender(file_path)