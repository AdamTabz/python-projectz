import pgzrun
import random
HEIGHT=840
WIDTH=1200
goku=Actor("goku.png")
goku.pos=(1100,400)
opps=[]
score=5
speed=10
pic=["eifel.png","cat.png","melon.png","bil.png"]


def draw():
    if score<0:
        screen.blit("done.png",(0,0))
        return
    screen.blit("background.png",(0,0))
    goku.draw()
    for opp in opps:
        opp.draw()
    screen.draw.text(str(score),(500,100),color=("black"))


def faster():
    global speed
    speed+=3
    clock.schedule(faster,10)



def update():
    global score
    if score<0:
                
        return
    if keyboard.up:
        goku.y-=10
    if keyboard.down:
        goku.y+=10
    for opp in opps:
        opp.x+=speed
        if opp.x==1200:
            opps.remove(opp)
        if opp.colliderect(goku):
            score-=1
            opps.remove(opp)    
           

def create():
    opp=Actor(random.choice(pic))    
    opp.y=random.randint(1, 840)
    opp.x=1
    opps.append(opp)
    clock.schedule(create, 0.5)


faster()
create()
pgzrun.go()