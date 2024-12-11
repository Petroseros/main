import pygame

from Character import Character

screen = pygame.display.set_mode((1000, 500))
character = Character()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(((255, 255, 255)))
    character.move()
    character.display(screen)
    pygame.display.flip()
