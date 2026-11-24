class shapes():
    def __init__(self, sides, name):
        self.sides = sides
        self.name = name
    def display(self):
        print(self.sides, self. name)


shape1=shapes("3","triangle")
shape2=shapes("4","square")
shape3=shapes("5", "pentagon")
shape1.display()

