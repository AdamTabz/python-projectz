import turtle
pen=turtle.Turtle()
screen=turtle.Screen()
list=["xxxxxxxxxxxxxxx",
      "xx   xx   xxxxx",
      "x  x f x    xxx",
      "xx  xx  xx   xx",
      "x          xxxx",
      "xxx xxxxx  xxxx",
      "xx  x   x    xx",
      "xx     xxxx   x",
      "xx x x  x   x x",
      "xx   xx xxxxx x",
      "xx xxxx    x  x",
      "x    xx  xxx xx",
      "xx    xx      x",
      "xx xx     xxxxx",
      "xxxxxxxxxxxxxxx"]
tilel=[]
for y in range(len(list)):
    for x in range(len(list[y])):
        tileX=-288+(x*24)
        tileY=288-(y*24)
        charecter=list[y][x]
        if charecter=="x":
            tile=turtle.Turtle()
            tile.shape("square")
            tile.up()
            tile.speed(0)
            tile.goto(tileX,tileY)
            tilel.append(tile)
        elif charecter=="f":
            food=turtle.Turtle()
            food.shape("circle")
            food.up()
            food.color("red")
            food.goto(tileX, tileY )
pen.up()
pen.shape("turtle")
def check():
    if pen.distance(food)<10:
        pen.write("you won!!", font=("arial", 25, "bold"))
def validmove(x,y):
    for tile in tilel:
        if x==tile.xcor()and y==tile.ycor():
            return False
    return True
def right():
    x=pen.xcor()
    x+=24
    y=pen.ycor()
    if validmove(x,y)==True:

        pen.goto(x,y)
    check()
screen.listen()
screen.onkey(right,"Right")

def left():
    x=pen.xcor()
    x-=24
    y=pen.ycor()
    if validmove(x,y)==True:

        pen.goto(x,y)
    check()
screen.listen()
screen.onkey(left,"Left")
def down():
    y=pen.ycor()
    y-=24
    x=pen.xcor()
    if validmove(x,y)==True:

        pen.goto(x,y)
    check()
screen.listen()
screen.onkey(down,"Down")

def up ():
    y=pen.ycor()
    y+=24
    x=pen.xcor()
    if validmove(x,y)==True:

        pen.goto(x,y)
    check()
screen.listen()
screen.onkey(up,"Up")
turtle.done()

