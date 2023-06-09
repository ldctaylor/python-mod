import random 
number = random.randrange(1,11)
play = "y"

while play != "no":
    user_number = int(input("Please enter an integer between 1 and 10: "))
    while number != user_number:
        if user_number < number:
            print("too low...")
        else:
            print("too high...")
        user_number = int(input("Make a guess: "))

    print("just right!")
    number = random.randrange(1,11)
    play = input("If you would like to stop playing, type no. Otherwise, we'll play again: ")
