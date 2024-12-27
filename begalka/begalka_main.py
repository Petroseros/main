import pygame
pygame.init()
from begalka.Chelovechek import Chelovechek
a = 0
chelovechek = Chelovechek()
screen = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()
running = True
while running:
    screen.fill((0, 0, 0))
    chelovechek.display(screen)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                chelovechek.up()


