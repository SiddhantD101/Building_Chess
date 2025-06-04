import pygame as p

p.init()
screen = p.display.set_mode((400, 400))
p.display.set_caption("Minimal Test")

running = True
while running:
    for event in p.event.get():
        if event.type == p.QUIT:
            running = False
    screen.fill((100, 150, 255))
    p.display.flip()

p.quit()
