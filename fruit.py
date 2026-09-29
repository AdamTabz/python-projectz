import pgzrun
import random
WIDTH=640
HEIGHT=640
basket=Actor("basket.png")
basket.pos=(300,550)
nugget=Actor("nugget.png")
nugget.pos=(random.randint(75, 575),50)
score=0

def draw():
    screen.blit("tree.jpg",(0,0))
    basket.draw()
    nugget.draw()
    screen.draw.text(str(score),(70,320))
def update():
    global score
    if keyboard.left:
        basket.x-=5
    if keyboard.right:
        basket.x+=5
    nugget.y+=5
    if nugget.colliderect(basket):
        score+=1
        nugget.pos=(random.randint(75, 575),50)
    if nugget.y>=640:
        score+=-1
        nugget.pos=(random.randint(75, 575),50)
 
    

pgzrun.go()