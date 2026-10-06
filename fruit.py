import pgzrun
import random
WIDTH=640
HEIGHT=640
basket=Actor("basket.png")
basket.pos=(300,550)

score=0
fruits=[]
pic=["fries.png", "nugget.png", "mac.png", "soda.png"]
def create():
    fruit=Actor(random.choice(pic))
    fruit.pos=(random.randint(75, 575),50)
    fruits.append(fruit)
    clock.schedule(create, 0.5)


def draw():
    if score<0:
        screen.blit("done.png",(0,0))
        return
    screen.blit("tree.jpg",(0,0))
    basket.draw()
    for fruit in fruits:
        fruit.draw()

    screen.draw.text(str(score),(70,320),color=("black"))

def update():
    global score
    if score<0:
            
        return
    if keyboard.left:
        basket.x-=5
    if keyboard.right:
        basket.x+=5
    for fruit in fruits:
        fruit.y+=10
        if fruit.colliderect(basket):
            score+=1
            fruits.remove(fruit)
        if fruit.y>=640:
            score+=-15
            fruits.remove(fruit)
       

 
create()    

pgzrun.go()