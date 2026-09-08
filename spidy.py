import pgzrun
import random
WIDTH=1000
HEIGHT=700
spidy=Actor("spidy.png")
spidy.pos=(random.randint(0,800),random.randint(0,500))
score=0

def draw():
    screen.blit("background.png",(0,0))
    spidy.draw()
    screen.draw.text(str(score),(10,10))
def move():
  spidy.pos=(random.randint(0,800),random.randint(0,500))
  clock.schedule(move,0.75)
def on_mouse_down(pos):
    global score
    if spidy.collidepoint(pos):
        score+=1
    else:
        score-=1
move()   
pgzrun.go()


