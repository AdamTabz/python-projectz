import pgzrun
WIDTH=1000
HEIGHT=700
spidy=Actor("spidy.png")
spidy.pos=(100,100)
def draw():
    screen.blit("background.png",(0,0))
    spidy.draw()
def on_mouse_down(pos):
    spidy.pos=(pos)

   



pgzrun.go()


