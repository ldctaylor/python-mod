Questions

2. Best practice re setting variables etc or just nesting complex calculations
3. battery usage with visual studio code


##Dictionaries Question
In examples of working with files, we created a reader_object:
```
    csv_reader = csv.reader(my_file, delimiter = " ") 
```

However in my solutions I find myself making a list before beginning to work with the data, as it seems many methods do not work on the reader_object. As an example, in the galaxies exercise (fileslesson/CSVExercise4.py) I created a file because I could not do the following step of converting strings to integers within the reader_object; I kept getting errors.
```
    with open("galaxies.csv") as my_file: 
        galaxies = list(csv.reader(my_file)) 

    for index in range(len(galaxies)):
        for galaxy in range(2):
            galaxies[index][galaxy] = int(galaxies[index][galaxy])  
```

I found myself doing the same in dictionaries/dictionariesq2.py because I coudln't use the lower() method on the csv_reader :
```
with open(file="../fileslesson/colours_865.csv") as coloursfile: 
    colours = list(csv.reader(coloursfile)) #create a list to work with

#change all coloours to uniform lowercase to assist matching
for colour in range(len(colours)):
    colours[colour][2] = colours[colour][2].lower()
```

I know it's 'fine' because it works, but what about best practice - am I missing something in the point of creating reader_objects, and am I doing something wrong if I'm unable to run basic methods on them? Why would you work with reader objects instead of creating lists, in terms of best practice?
