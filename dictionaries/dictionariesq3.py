#Read the colour data from colours_20_simple.csv (available in the repo linked above) and save the data in a dictionary where each key is a hex code and each value is the corresponding English name
import csv

with open("../fileslesson/colours_20_simple.csv","r") as file: 
    colours = list(csv.reader(file))

colour_dict = {}

for _ in range(1,len(colours)):
    colour_dict[colours[_][1]] = colours[_][2]

print(colour_dict)