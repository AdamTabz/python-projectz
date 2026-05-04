import turtle
import random
blns=[]
pen=turtle.Turtle()
pen.shape("triangle")
pen.up()
def bln():
    balloon=turtle.Turtle()
    balloon.hideturtle()
    balloon.shape("circle")
    balloon.color("red")
    balloon.up()
    balloon.goto(random.randint(-240, 240),240)
    blns.append(balloon)
    balloon.showturtle()
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
score=0


while True:
    num=random.randint(1,10)
    if num==9:
        bln()
    for balloon in blns:
            balloon.sety(balloon.ycor()-8)
            
            if balloon.distance(pen)<20:
                 balloon.hideturtle()
                 blns.remove(balloon)
                 score=score+1
                 turtle.clear()
                 turtle.hideturtle()
                 turtle.write(str(score))

                 

    