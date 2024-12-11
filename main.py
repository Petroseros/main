import pygame

from Character import Character
from Tube import Tube

screen = pygame.display.set_mode((1000, 600))
clock = pygame.time.Clock()
character = Character()
tube = Tube()
tube1 = Tube()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                character.jump()
    screen.fill((0, 0, 0))
    character.move()
    character.display(screen)
    tube.move()
    tube.display(screen)
    pygame.display.flip()
    clock.tick(10)
