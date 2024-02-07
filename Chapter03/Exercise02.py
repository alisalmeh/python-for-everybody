# Rewrite your pay program using try and except so that your
# program handles non-numeric input gracefully by printing a message
# and exiting the program.
try:
    hours = float(input('Enter hours: '))
    rate = float(input('Enter rate: '))
except:
    print('Error, please enter numeric input')    
    quit()

if hours > 40:
    gross_pay = (40 * rate) + (hours - 40) * rate * 1.5
else:
    gross_pay = hours * rate

print('Pay:', gross_pay)