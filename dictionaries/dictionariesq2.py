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
    colours = csv.reader(coloursfile) #create a list to work with
    
    for colour in colours:
        colour[2] = colour[2].lower() #change all coloours to uniform lowercase to assist matching
        for _ in colour_counts.keys():
            if _ in colour[2]:
                colour_counts[_] = colour_counts[_]+1
print(colour_counts)