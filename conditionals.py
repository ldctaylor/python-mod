#Boolean

name = "Leah"
age = 42
height = 1.57
is_raining = True
my_variable2 = False

print(is_raining)
print(type(is_raining))

#Boolean Comparators
# == equal to (one equal sign means ASSIGNMENT)
# != not equal to 
# <
# >=

print(5 > 3)
print("Leah"=="Leah")
print("Leah"=="leah")

#Mathematical Operators - Addition, Division, Subtraction, Multiplication
#Boolean Operators - not, and, or

is_sunny = True
is_warm = True
print(not(is_sunny))
print(is_sunny and is_warm)
print(is_sunny or is_warm)

#Conditionals

#python tabs should be four spaces, for conditionals/functions etc. If you don't put the spaces, it won't read it as part of the if statement
#temperature needs to be declared before the if statement, because the code runs in "real time" it isn't compiled first
#the line about the dog being cutest, has nothing to do with the if statement, will print regardless, because it's not indented.
temperature = 20
if temperature < 18:
    print("Weather is too cold")
#else needs to be at the start of the line again or it won't work
else:
    print("Weather is nice")
print("My dog is the cutest of all")

#Adding in elif (else if)
temperature = 18
if temperature <= 18:
    print("Weather is too cold")
    print("I want to stay home")
elif temperature > 28: #if the if statement is false, it will check elif, then if that's false it will check else
    print("Weather is too hot")
else: 
    print("Weather is nice")
#you can have multiple elifs but only one else