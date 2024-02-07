# Rewrite your pay computation to give the employee 1.5
# times the hourly rate for hours worked above 40 hours.
hours = float(input('Enter hours: '))
rate = float(input('Enter rate: '))

if hours > 40:
    gross_pay = (40 * rate) + (hours - 40) * rate * 1.5
else:
    gross_pay = hours * rate

print('Pay:', gross_pay)