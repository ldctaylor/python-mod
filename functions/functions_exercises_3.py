#Write a function that accepts one argument (an integer) and returns True when thatargument is odd and False when that argument is even. You can use the same formatas the starter code in the previous exercise. Just remember - you're returning theresult, not printing it!

some_int = int(input("Give me a number "))

def is_it_odd(some_int):
    return some_int % 2 == 1