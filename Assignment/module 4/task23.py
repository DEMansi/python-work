
# Python class named Rectangle constructed by a length and 
#width and a method which will compute the area of a rectangle 

class Rectangle():
    def __init__(self, l, w):
        self.length = l
        self.width  = w

    def area(self):
        return self.length*self.width

obj= Rectangle(12, 10)
print("The Rectangle Area is: ",obj.area())
