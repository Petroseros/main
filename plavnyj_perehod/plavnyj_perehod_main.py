import pygame
from plavnyj_perehod.Cvet import Cvet
a = 0
cvet = Cvet()
screen = pygame.display.set_mode((255, 50))
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
    screen.fill((255, 255, 255))

    cvet.display(screen)
    cvet.move()


