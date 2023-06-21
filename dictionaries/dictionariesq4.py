#Modify your code from the previous exercise to save both the English name and RGB code in a list as the value for the corresponding hex code.
import csv

with open("../fileslesson/colours_20_simple.csv","r") as file: 
    colours = list(csv.reader(file))

colour_dict = {}

for _ in range(1,len(colours)):
    colour_dict[colours[_][1]] = [colours[_][0],colours[_][2]]

print(colour_dict)