"""
This program counts the distribution of the hour of the day
for each of the messages. You can pull the hour from the “From” line
by finding the time string and then splitting that string into parts using
the colon character. Once you have accumulated the counts for each
hour, print out the counts, one per line, sorted by hour as shown below.

python timeofday.py
Enter a file name: mbox-short.txt

04 3
06 1
07 1
09 2
10 3
11 6
14 1
15 2
16 4
17 2
18 1
19 1
"""
file_name = input('Enter a file name: ')
try:
    file_handle = open(file_name, 'r')
    hours = dict()

    for line in file_handle:
        words = line.split()
        if len(words) == 0 or words[0] != 'From' : continue
        time = words[5]
        colon_pos = time.find(':')
        hour = time[ :colon_pos]
        hours[hour] = hours.get(hour, 0) + 1

    for key, val in sorted(hours.items()): 
        print(key, val)
    
except FileNotFoundError:
    print(f"File '{file_name}' not found.")
    quit()