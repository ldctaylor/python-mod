import csv

colour_counts = {
    "blue": 0,
    "green": 0,
    "yellow": 0,
    "red": 0,
    "purple": 0,
    "orange": 0,
}

with open(file="../fileslesson/colours_865.csv") as coloursfile: 
    colours = list(csv.reader(coloursfile)) #create a list to work with

#change all coloours to uniform lowercase to assist matching
for colour in range(len(colours)):
    colours[colour][2] = colours[colour][2].lower()

#for each row of the colours file, if the dictionary key is in the name of the colour, add 1 to the value of that key
for row in range(len(colours)):
    for _ in colour_counts.keys():
        if _ in colours[row][2]:
            colour_counts[_] = colour_counts[_]+1
print(colour_counts)