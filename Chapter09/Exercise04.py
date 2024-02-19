"""
Add code to the above program to figure out who has the
most messages in the file. After all the data has been read and
the dictionary has been created, look through the dictionary using a maximum
loop (see Chapter 5: Maximum and minimum loops) to find who has
the most messages and print how many messages the person has.

Enter a file name: mbox-short.txt
cwen@iupui.edu 5
Enter a file name: mbox.txt
zqian@umich.edu 195
"""
def count_messages_from_each_sender(file_name):
    try:
        file_handle = open(file_name, 'r')
        email_addresses = {}

        for line in file_handle:
            if line.startswith('From '):
                email = line.split()[1]
                email_addresses[email] = email_addresses.get(email, 0) + 1

        return email_addresses
    
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
        quit()

def find_max_message(email_addresses):
    max_email = None
    max_count = None
    
    for email, count in email_addresses.items():
        if max_count is None or max_count < count:
            max_count = count
            max_email = email  

    print(max_email, max_count)

file_path = input('Enter file name: ')
find_max_message(count_messages_from_each_sender(file_path))