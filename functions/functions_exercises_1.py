#Write a function called get_integer that takes a string as its argument, and uses thatstring to prompt the user to enter an integer. Your function should return the integersupplied by the user.

prompt = "Could I please have an integer ? "

def get_integer(prompt):
    return(input(prompt))

user_input = get_integer(prompt)

print(f"So your integer is {user_input}? Thanks!")