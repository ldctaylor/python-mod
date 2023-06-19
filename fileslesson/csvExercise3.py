import csv

green = 0
red = 0
blue = 0
yellow = 0

with open(file="colours_20_simple.csv") as my_file: 
    csv_reader = csv.reader(my_file) #create a reader object
    for row in csv_reader:
        if "red" in row[2].lower():
            red = red + 1
        if "green" in row[2].lower():
            green = green + 1
        if "blue" in row[2].lower():
            blue = blue + 1
        if "yellow" in row[2].lower():
            yellow = yellow + 1

    print(f"Red: {red}")
    print(f"green: {green}")
    print(f"blue :{blue}")
    print(f"yellow: {yellow}")
