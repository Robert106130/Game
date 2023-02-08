bootl = Actor('bootl')
bootl.pos = 100,50

Width = 500
Height = bootl.height + 300

def draw():
    screen.fill((255, 102, 0))
    bootl.draw()

def update():
    bootl.left += 2
    if bootl.left > Width:
        bootl.right = 0

def on_mouse_down(pos):
    if bootl.collidepoint(pos):
        print("Eek!")
    else:
        print("You missed me!")
