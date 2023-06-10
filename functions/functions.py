#Lesson on functions. 
#Function - an activity that is natural to or the purpose of a person or thing. 

#Function's we've already seen
#input() #len() #int() #print()
#every function has brackets


#Task Separation

#without a function:
# name = input("What's your name? ")
# age = int(input("How old are you? "))
# if age >= 18:
#     print("Welcome")
# else:
#     print("You can not enter.")

#Function Definition
def ask_user_name():
    print("Now function is entered")
    name = input("What's your name? ")
    print(name)
    return name 
    print("hello") #doesn't get executed - return STOPS the function immediately

def ask_user_age():
    age = int(input("How old are you? "))
    if age >= 18:
        print("Welcome")
    else:
        print("You can not enter.")

#Calling a Function
print("Hello")
ask_user_name()

#Global / Local Variables

#parameters

def add(number1, number2): #when we call this function, it expects two values into it. These are the PARAMETERS. At this point they don't have values as it hasn't been called yet. 
    result = number1 + number2 #local variable
    return result

answer = add(2,3) #global variable
print(answer)
print(add(2,3))