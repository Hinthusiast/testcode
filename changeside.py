class Square:
    def __init__(self,side):
        self.s1 = side

    def change_size(self):
        newSide=int(input('Please enter new dimension:'))
        self.s1-=newSide
sqr=Square(125)
sqr.change_size()




