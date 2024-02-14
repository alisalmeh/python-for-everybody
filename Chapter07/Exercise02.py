"""
Write a program to prompt for a file name, and then read
through the file and look for lines of the form:

X-DSPAM-Confidence: 0.8475

When you encounter a line that starts with “X-DSPAM-Confidence:”
pull apart the line to extract the floating-point number on the line.
Count these lines and then compute the total of the spam confidence
values from these lines. When you reach the end of the file, print out
the average spam confidence.

Enter the file name: mbox.txt
Average spam confidence: 0.894128046745

Enter the file name: mbox-short.txt
Average spam confidence: 0.750718518519
"""
def calculate_average_spam_confidence(file_name):
    str = 'X-DSPAM-Confidence:'
    count = 0
    sum = 0
    
    try:
        file = open(file_name)
    except:
        print('File not found')
        quit()
    
    for line in file:
        if line.startswith(str):
            count += 1
            colon_pos = line.find(':')
            extracted_num = float(line[colon_pos + 1 : ].lstrip())
            sum += extracted_num
        else:
            continue
    
    print(f'Average spam confidence: {round(sum / count, 12)}')

file_name = input('Enter a file name: ')
calculate_average_spam_confidence(file_name)