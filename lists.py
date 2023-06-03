digits = [1,2,3,4,5]
print(digits[0:4]) #start is inclusive, end is exclusive
print(digits[3:])
print(digits[3:-1])
print(digits[3:-2]) 
print(digits[0:5:1]) #prints everything
print(digits.pop(1)) #remove and return the value in index number
digits[1] = str(digits[1]) + " boo"
print(digits)