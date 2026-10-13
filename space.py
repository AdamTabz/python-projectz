import pgzrun
HEIGHT=850
WIDTH=786 
ship=Actor("ship.png")
ship.pos=(350,800)
opps=[]
def draw():
    screen.blit("space.png",(0,0))
    ship.draw()
    for opp in opps:
        opp.draw()
def update():
    if keyboard.left:
        ship.x-=5
    if keyboard.right:
        ship.x+=5
    for opp in opps:
        opp.y+=1
def newopp():
    opp=Actor("opp.png",(150, 150))
    opps.append(opp)
    clock.schedule(newopp,2.5)
newopp()
pgzrun.go()