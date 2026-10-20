import pgzrun
HEIGHT=850
WIDTH=786 
ship=Actor("ship.png")
ship.pos=(350,800)
opps=[]
lives=3
bullets=[]

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

def newopp():
    for i in range(4):

        opp=Actor("opp.png",(100+i*170, 150))
        opps.append(opp)
    clock.schedule(newopp,2)
def on_key_down(key):
    if key==keys.SPACE:
        pew=Actor("pew.png",(ship.x,ship.y))
        bullets.append(pew)
newopp()
pgzrun.go()