# Write a program to prompt the user for hours and rate per hour to compute gross pay.
hours = float(input('Enter hours: '))
rate = float(input('Enter rate: '))

gross_pay = round(hours * rate, 2)
print('Pay:', gross_pay)