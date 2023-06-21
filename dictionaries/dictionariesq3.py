#Read the colour data from colours_20_simple.csv (available in the repo linked above) and save the data in a dictionary where each key is a hex code and each value is the corresponding English name
import csv

colour_dict = {}

with open("../fileslesson/colours_20_simple.csv","r") as file: 
    colours = csv.reader(file)
    next(colours) #skip header row
    for colour in colours:
        colour_dict[colour[1]] = colour[2]

print(colour_dict)