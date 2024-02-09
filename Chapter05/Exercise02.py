"""
Write another program that prompts for a list of numbers
as above and at the end prints out both the maximum and minimum of
the numbers instead of the average.
"""
total = 0
count = 0
minimum = None
maximum = None

while True:
    try:
        user_input = input('Enter a number: ')
        if user_input == 'done':
            print(total, count, minimum, maximum)
            break
        number = float(user_input)
        total += number
        count += 1
        if minimum is None or number < minimum:
            minimum = number
        elif maximum is None or number > maximum:
            maximum = number
    except:
        print('Invalid input')