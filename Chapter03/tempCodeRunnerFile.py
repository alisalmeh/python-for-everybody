# Rewrite your pay computation to give the employee 1.5
# times the hourly rate for hours worked above 40 hours.
hours = float(input('Enter hours: '))
rate = float(input('Enter rate: '))

pay_for_40_hours_work = 40 * rate
normal_pay = hours * rate
overtime_pay = (hours - 40) * rate * 1.5

if hours > 40:
    gross_pay = pay_for_40_hours_work + overtime_pay
else:
    gross_pay = normal_pay

print('Pay:', gross_pay)