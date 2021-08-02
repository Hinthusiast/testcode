class Square():
    square_list=[]
    def __init__(self, s1):
        self.s1 = s1
        self.square_list.append(s1)

    def calculate_perimeter(self):
        return self.s1 * 4

    def change_size(self, new_size):
        self.s1 += new_size

