
class Square:
    def __init__(self,side):
        self.s1 = side

    def calculate_perimeter(self):
        return self.s1**2
        
    def change_size(self):
        newSide=int(input('Please enter new dimension:'))
        self.s1-=newSide

sqr = Square(45)
print(sqr.calculate_perimeter())
sqr.change_size()
print(sqr.calculate_perimeter())

