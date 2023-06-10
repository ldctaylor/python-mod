#Write a function called celcius_convert that takes a number representing thetemperature in Farenheit as its argument, and returns a float representing thetemperature in Celcius.

temp_in_fahrenheit = float(input("Please give me the temperature in fahrenheit "))

def celcius_convert(temp_in_fahrenheit):
    return (temp_in_fahrenheit - 32) * 5/9

print(celcius_convert(temp_in_fahrenheit))




