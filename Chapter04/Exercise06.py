"""
Rewrite your pay computation with time-and-a-half for overtime
and create a function called computepay which takes two parameters
(hours and rate).
"""
try:
    hours = float(input('Enter hours: '))
    rate = float(input('Enter rate: '))
except:
    print('Error, please enter numeric input')    
    quit()

def computepay(hours, rate):
    if hours > 40:
        return (40 * rate) + (hours - 40) * rate * 1.5
    else:
        return hours * rate

gross_pay = computepay(hours, rate)
print('Pay:', gross_pay)