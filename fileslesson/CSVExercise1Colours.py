import csv

with open(file="colours_20_simple.csv") as my_file: 
    csv_reader = csv.reader(my_file) #create a reader object
    for row in csv_reader:
        print(f"{row[0]} {row[1]} {row[2]}")