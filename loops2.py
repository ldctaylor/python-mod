 # the challenge is to ask the user to enter an integer number, then print all the odd numbers between 0 and that number (inclusive). Ignore negative numbers.

number = int(input("Enter an integer number: "))
i = 0 

while i <= number:
    if i % 2 == 1:
        print(i)
    i += 1
    