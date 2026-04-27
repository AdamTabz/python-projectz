import turtle


pen=turtle.Turtle()

pen.speed(100)
pen.up()
turtle.colormode(255)
pen.up()
pen.right(90)
pen.forward(100)
pen.left(180)

pen.shape("circle")
while True:
   for i in range(180):
     pen.forward(1)
   for i in range(180):
     pen.backward(1)