import pgzrun
import random
HEIGHT=850
WIDTH=786 
ship=Actor("ship.png")
ship.pos=(350,800)
opps=[]
lives=3
bullets=[]
lasers=[]


def draw():
    if lives==0:
        screen.blit("done.png",(0,0))
        return
    screen.blit("space.png",(0,0))
    ship.draw()
    for opp in opps:
        opp.draw()
    screen.draw.text("lives"+str(lives),(300,100))
    for pew in bullets:
        pew.draw()
    for laser in lasers:
        laser.draw()
def update():
    global lives
    if lives==0:
            
        return
    if keyboard.left:
        ship.x-=5
    if keyboard.right:
        ship.x+=5
    for opp in opps:
        opp.y+=1
    for opp in opps:
        if opp.colliderect(ship):
            lives-=1
            opps.remove(opp)
    for pew in bullets:
        pew.y-=4
        for opp in opps:
            if pew.colliderect(opp):
                opps.remove(opp)
                bullets.remove(pew)
    for laser in lasers:
        laser.y+=4
    for laser in lasers:
        if laser.colliderect(ship):
                lives-=1
                lasers.remove(laser)
def oppshoot():
    shooter=random.choice(opps)
    laser=Actor("laser.png",shooter.pos)
    lasers.append(laser)
    clock.schedule(oppshoot, 0.2)

def newopp():
    for i in range(4):

        opp=Actor("opp.png",(100+i*170, 150))
        opps.append(opp)
    clock.schedule(newopp,3.4)
def on_key_down(key):
    if key==keys.SPACE:
        pew=Actor("pew.png",(ship.x,ship.y))
        bullets.append(pew)
newopp()
oppshoot()
pgzrun.go()