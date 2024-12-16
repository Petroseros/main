import pygame

from flappy_bird.Bird import Bird
from Tube import Tube
a = 0
screen = pygame.display.set_mode((1800, 600))
clock = pygame.time.Clock()
bird = Bird()
tube = Tube(1850)
tube1 = Tube(2450)
tube2 = Tube(3050)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird.jump()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
    screen.fill((0, 0, 0))

    bird.move()
    bird.display(screen)

    tube.move()
    tube.display(screen)
    tube.teleportation()
    if tube.tunumber():
        a += 1
        print(a)

    tube1.move()
    tube1.display(screen)
    tube1.teleportation()
    if tube1.tunumber():
        a += 1
        print(a)

    tube2.move()
    tube2.display(screen)
    tube2.teleportation()
    if tube2.tunumber():
        a += 1
        print(a)

    pygame.display.flip()
    clock.tick(50)
