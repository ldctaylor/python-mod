#Ask the user for an integer. Using a for loop, add up every number from 0 up to thatinteger, and print the result.

input = int(input("Please give me an integer: "))
sum = 0 

for _ in range(0,input + 1):
    sum = sum + _

print(sum)
