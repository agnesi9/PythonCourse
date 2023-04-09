#Create a class named Rectangle that has the following attributes: width and height. 
#It should also have methods called area() and perimeter() that return the area and perimeter of the rectangle, respectively.

class Rectangle:
    def __init__(self, width:int, height:int) -> None:
        self.width = width
        self.height = height

    def area(self):
        return self.width*self.height
    
    def perimeter(self):
        return 2*self.height+2*self.width
    
    def __str__(self) -> str:
        return "Area: " + str(Rectangle.area(self)) + ", perimeter: " + str(Rectangle.perimeter(self))
    
rect1 = Rectangle(2,5)
print(rect1)

