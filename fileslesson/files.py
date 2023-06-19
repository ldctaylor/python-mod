import csv

# open(file="file.csv", mode="r", encoding="utf-8") #specifying parameter = allows you to enter params in different order
# open(file="file.csv") #this is identical to the expression above because mode is r as default, and encoding is utf-8 as default too.

with open(file="file.csv") as my_file: #use with to prevent data leakage - file closes after
    print(my_file) #prints <_io.TextIOWrapper name='file.csv' mode='r' encoding='UTF-8'>
    csv_reader = csv.reader(my_file, delimiter = " ") #create a reader object
    for row in csv_reader:
        print(row)

population = []
with open(file="file.csv") as my_file: #use with to prevent data leakage - file closes after
    print(my_file) #prints <_io.TextIOWrapper name='file.csv' mode='r' encoding='UTF-8'>
    csv_reader = csv.reader(my_file, delimiter = " ") #create a reader object
    for row in csv_reader:
        population.append(row)
    print(population)

    for word in population:
        print(f"First word is{word[0]}")

with open(file="writeable.csv", mode = "w") as my_file:
    csv_writer = csv.writer(my_file)
    csv_writer.writerow(["item1","item2"])

    for item in population:
        csv_writer.writerow(item)
    
    for item in population:
        csv_writer.writerow([item[0], item[1]])
