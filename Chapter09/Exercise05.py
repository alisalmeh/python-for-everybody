"""
This program records the domain name (instead of the
address) where the message was sent from instead of who the mail came
from (i.e., the whole email address). At the end of the program, print
out the contents of your dictionary.

python schoolcount.py
Enter a file name: mbox-short.txt
{'media.berkeley.edu': 4, 'uct.ac.za': 6, 'umich.edu': 7,
'gmail.com': 1, 'caret.cam.ac.uk': 1, 'iupui.edu': 8}
"""
import email


def count_messages_from_each_domain(file_name):
    try:
        file_handle = open(file_name, 'r')
        domains = {}

        for line in file_handle:
            if line.startswith('From '):
                email = line.split()[1]
                domain = email.split('@')[1]
                domains[domain] = domains.get(domain, 0) + 1

        print(domains)
    
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
        quit()

file_path = input('Enter file name: ')
count_messages_from_each_domain(file_path)