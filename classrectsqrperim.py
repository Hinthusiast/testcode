
class Rectangle:
    def __init__(self, width, length):
        self.width = width
        self.length = length

    
    def calculate_perimeter(self):
        return self.width+self.length+self.width+self.length
        
    
    
    
class Square:
    def __init__(self,side):
        self.s1 = side

    def calculate_perimeter(self):
        return self.s1*4


ret=Rectangle(4,5)
sqr=Square(4)
print(ret.calculate_perimeter())
print(sqr.calculate_perimeter())