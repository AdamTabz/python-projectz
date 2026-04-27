import turtle
import random
pen=turtle.Turtle()
pen.shape("triangle")
pen.up()
balloon=turtle.Turtle()
balloon.shape("circle")
balloon.color("red")
balloon.up()
balloon.goto(random.randint(-240, 240),240)
screen=turtle.Screen()
screen.setup(500,500)
pen.left(90)
pen.goto(0,-230)
def left():
    x=pen.xcor()
    x-=24
    y=pen.ycor()
    pen.goto(x,y)
screen.listen()
screen.onkey(left,"Left")

def right():
    x=pen.xcor()
    x+=24
    y=pen.ycor()
    pen.goto(x,y)
screen.listen()
screen.onkey(right,"Right") 
turtle.done()
pen
    