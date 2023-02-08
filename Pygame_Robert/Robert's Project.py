bootl = Actor('bootl')
bootl.pos = 100,50

Width = 500
Height = bootl.height + 300

def draw():
    screen.fill((255, 102, 0))
    bootl.draw()

def update():
    bootl.left + bootl.left + 2
    if bootl.left > Width:
        bootl.right = 0
