import pygame
from begalka.Red import Red
from begalka.Blue import Blue
from begalka.Wall1 import Wall1
from begalka.Wall2 import Wall2
pygame.init()

screen = pygame.display.set_mode((1000, 1000))
clock = pygame.time.Clock()

red = Red()
blue = Blue()
wall1 = Wall1()
wall2 = Wall2()

running = True
while running:

    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    red.move()
    red.display(screen)
    red.tele(wall1,wall2)

    blue.move()
    blue.display(screen)
    blue.tele(wall1,wall2)

    wall1.move()
    wall1.display(screen)

    wall2.move()
    wall2.display(screen)

    pygame.display.flip()