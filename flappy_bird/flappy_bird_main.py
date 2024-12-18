import pygame

from flappy_bird.Bird import Bird
from Tube import Tube
from Cloud import Cloud
a = 0
screen = pygame.display.set_mode((1800, 600))
clock = pygame.time.Clock()

bird = Bird()

tube = Tube(1800)
tube1 = Tube(2400)
tube2 = Tube(3000)

cloud = Cloud(1800)
cloud1 = Cloud(2100)
cloud2 = Cloud(2400)
cloud3 = Cloud(2700)
cloud4 = Cloud(3000)
cloud5 = Cloud(3300)

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
    screen.fill((73, 178, 216))

    cloud.move()
    cloud.display(screen)
    cloud.teleportation()

    cloud1.move()
    cloud1.display(screen)
    cloud1.teleportation()

    cloud2.move()
    cloud2.display(screen)
    cloud2.teleportation()

    cloud3.move()
    cloud3.display(screen)
    cloud3.teleportation()

    cloud4.move()
    cloud4.display(screen)
    cloud4.teleportation()

    cloud5.move()
    cloud5.display(screen)
    cloud5.teleportation()

    bird.move()
    bird.display(screen)

    tube.move()
    tube.display(screen)
    tube.teleportation()
    if tube.tunumber():
        a += 1
        print(a)
    if tube.death(bird):
        running = False

    tube1.move()
    tube1.display(screen)
    tube1.teleportation()
    if tube1.tunumber():
        a += 1
        print(a)
    if tube1.death(bird):
        running = False

    tube2.move()
    tube2.display(screen)
    tube2.teleportation()
    if tube2.tunumber():
        a += 1
        print(a)
    if tube2.death(bird):
        running = False

    pygame.display.flip()
    clock.tick(50)