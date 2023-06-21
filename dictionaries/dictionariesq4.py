#Modify your code from the previous exercise to save both the English name and RGB code in a list as the value for the corresponding hex code.
import csv

colour_dict = {}

with open("../fileslesson/colours_20_simple.csv","r") as file: 
    colours = csv.reader(file)
    next(colours) #skip header row
    for colour in colours:
        colour_dict[colour[1]] = [colour[0],colour[2]]

print(colour_dict)
