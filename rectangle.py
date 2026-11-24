class rectangle():
    
    def __init__(self, length, width):
        self.length = length
        self.width = width
  
    def display(self):
        print(self.length, self. width)
   
    def area(self):
        print(self.length*self.width)
    def perimeter(self):
        print(self.length*2+self.width*2)
    
rectangle1=rectangle(15,20)
rectangle2=rectangle(18,25)
rectangle1.area()
rectangle1.perimeter()
