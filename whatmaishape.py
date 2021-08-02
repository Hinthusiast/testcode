class Shape(): 
    def what_am_i(self): 
        print("I am a shape.") 

class Rectangle(Shape): 
    def __init__(self, width, length):
        self.width = width 
        self.length = length 

    
class Square(Shape): 
    def __init__(self, s1):
        self.s1 = s1 


rect = Rectangle(20, 50)
sqr = Square(29)
rect.what_am_i()
sqr.what_am_i()