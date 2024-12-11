import pygame.draw

import random

class Character:
    def __init__(self):
        self.x = 1
        self.y = 100
        self.side = 50
        self.speedx = 1
        self.speedy = 1
    def display(self, screen):
        pygame.draw.rect(screen, ((random.randint(0, 255)), (random.randint(0, 255)), (random.randint(0, 255))), (self.x, self.y, self.side, self.side))

    def move(self):
        self.x += self.speedx
        self.y += self.speedy
        if self.x == 950:
            self.speedx *= -1
        if self.x == 0:
            self.speedx *= -1
        if self.y == 450:
            self.speedy *= -1
        if self.y == 0:
            self.speedy *= -1