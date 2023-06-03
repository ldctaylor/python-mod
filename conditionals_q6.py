#Conditionals exercise 6
email = input("Please enter your email address: ")

if "@" in email and "." in email:
    print("Email is valid")
else:
    print("Invalid")