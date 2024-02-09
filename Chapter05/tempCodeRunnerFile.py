user_input = None
count = 0
sum = 0

while True:
    try:
        user_input = input('Enter a number: ')
        if user_input == 'done':
            print(sum, count, sum / count)
            break
        number = float(user_input)
        count += 1
        sum = number + sum
    except:
        print('Bad Input')