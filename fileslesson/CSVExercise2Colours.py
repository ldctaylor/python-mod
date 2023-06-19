import csv

with open(file="colours_20_simple.csv") as my_file: 
    csv_reader = csv.reader(my_file) #create a reader object
    next(my_file)
    for row in csv_reader:
        print(f"{row[2]}, Hex: {row[1]}, RGB: {row[0]}")