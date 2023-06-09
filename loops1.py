number = input("Give me a number ")
sum = 0

while number != "":
    sum = sum + int(number)
    number = input("Give me a number ")

print(f"Your numbers sum to {sum}")