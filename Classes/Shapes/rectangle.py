class rectangle():
    
    def __init__(self, length, width):
        self.length = length
        self.width = width
        self.area = 0
        self.perimeter = 0
       
    def calc_area(self):
        self.area = self.length * self.width
        return self.area
    
    def calc_perimeter(self):
        self.perimeter = self.length * self.width + 2
        return self.perimeter
    
    def __str__(self):
        return f"The rectangle has a length of {self.length} and a width of {self.width}. " \
               f"The perimeter is {self.perimeter} and the area is {self.area}."
    




