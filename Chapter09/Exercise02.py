"""
Write a program that categorizes each mail message by
which day of the week the commit was done. To do this look for lines
that start with “From”, then look for the third word and keep a running
count of each of the days of the week. At the end of the program print
out the contents of your dictionary (order does not matter).

Sample Line:
From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008

Sample Execution:
python dow.py
Enter a file name: mbox-short.txt
{'Fri': 20, 'Thu': 6, 'Sat': 1}
"""
def day_count (file_path):
    try:
        handle_file = open(file_path, 'r')
        days = {}

        for line in handle_file:
            words = line.split()
            if line.startswith('From ') and len(words) >= 3:
                day = words[2]
                days[day] = days.get(day, 0) + 1

        return days
    
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        quit()

file_path = input('Enter a file name: ')
print(day_count(file_path))