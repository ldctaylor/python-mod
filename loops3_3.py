#Save a list of numbers to a variable in your script, and then use a for loop to print thesum of all the numbers in the list

list = [-3,-5,9,1]
sum = 0

for _ in list:
    sum = sum + _

print(sum)