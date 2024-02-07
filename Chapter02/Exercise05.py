# Write a program which prompts the user for a Celsius temperature, convert the temperature to Fahrenheit, 
# and print out the converted temperature.
celsius = float(input('Enter temperature in celcius: '))
farenheit = (celsius * 1.8) + 32
print('Temperature:', farenheit, 'farenheit')