#here I will print the times table for a given number. 

number = input("Give me an integer please: ")

for _ in range(1,11):
    print(f"{number} * {_} = {(_ * int(number))}")
