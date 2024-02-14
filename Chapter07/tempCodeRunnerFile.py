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
    
    return 'Average spam confidence:', sum / count

file_name = input('Enter a file name: ')
calculate_average_spam_confidence(file_name)