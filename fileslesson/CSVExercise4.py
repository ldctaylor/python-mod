import csv

with open(file="galaxies.csv") as my_file: #use with to prevent data leakage - file closes after
    csv_reader = csv.reader(my_file) #create a reader object
    for row in csv_reader:
        print(row[1])
    max = max(csv_reader[1])
    print(f"The max is {max}")