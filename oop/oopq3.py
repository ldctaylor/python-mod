import math

class Rectangle():

    def __init__(self,width,height):
        self.width = float(width)
        self.height = float(height)

    def area(self,width,height):
        return width * height
    
    def perimeter(self,width,height):
        return width*2 + height*2
    
    def diagonal(self,width,height):
        return math.sqrt(width**2 + height**2)
    
    def is_square(self,width,height):
        if width == height:
            return "The rectangle is a square"
        else:
            return "The rectangle is not a square"

rect1 = Rectangle(10,5)

print(rect1.is_square(5,6))

