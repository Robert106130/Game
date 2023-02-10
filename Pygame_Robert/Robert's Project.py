bootl = Actor('bootl')
bootl.pos = 100,50

WIDTH = 300
HEIGHT = bootl.height + 300

def draw():
    screen.fill((255, 102, 0))
    bootl.draw()

def update():
    bootl.left += 2
    if bootl.left > WIDTH:
        bootl.right = 0

def on_mouse_down(pos):
    if bootl.collidepoint(pos):
        print("Eek!")
    else:
        print("You missed me!")
def on_mouse_down(pos):
    if bootl.collidepoint(pos):
        sound.eep.play()
        bootl.image = 'bootl'
