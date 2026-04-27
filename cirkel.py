import turtle
import random
import time
pen=turtle.Turtle()
pen.speed(100)

turtle.colormode(255)
pen.up()
pen.right(90)
pen.forward(100)
pen.left(90)
pen.down()
while True:
    pen.clear()
    pen.color(random.randint(0,255), random.randint(0,255), random .randint(0,255))
    pen.begin_fill()
    pen.circle(10)
    
    
    pen.end_fill()
    time.sleep(0.5)
    pen.up()
    pen.forward(30)
    pen.left(10)
    pen.down()

