import pygame
pygame.init()
from flappy_bird.Bird import Bird
from Tube import Tube
from Cloud import Cloud
a = 0
screen = pygame.display.set_mode((1800, 600))
clock = pygame.time.Clock()
font = pygame.font.SysFont("comicsans", 30)
follow = font.render(str(a), True, (255, 255, 255), (0, 0, 0))

bird = Bird()

tube1 = Tube(1800)
tube2 = Tube(2400)
tube3 = Tube(3000)

cloud1 = Cloud(1800)
cloud2 = Cloud(2100)
cloud3 = Cloud(2400)
cloud4 = Cloud(2700)
cloud5 = Cloud(3000)
cloud6 = Cloud(3300)

clouds = [cloud1, cloud2, cloud3, cloud4, cloud5, cloud6]
tubes = [tube1,tube2,tube3]

running = True
while running:
    screen.blit(follow, (0, 0))
    pygame.display.update()
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

    for cloud in clouds:
        cloud.move()
        cloud.display(screen)
        cloud.teleportation()

    bird.move()
    bird.display(screen)
    if bird.death(tubes):
        running = False

    for tube in tubes:
        tube.move()
        tube.display(screen)
        tube.teleportation()
        if tube.tunumber():
            a += 1
            print(a)

    pygame.display.flip()
    clock.tick(50)