import pygame.draw

import random

class Tube:
    def __init__(self, x):
        self.x = x
        self.speed = 10
        self.width = 50
        self.y = 0
        self.y2 = 400
        self.height = 200
        self.height2 = 200

    def display(self, screen):
        pygame.draw.rect(screen, (225, 225, 225), (self.x, self.y, self.width, self.height))
        pygame.draw.rect(screen, (225, 225, 225), (self.x, self.y2, self.width, self.height2))

    def move(self):
        self.x -= self.speed

    def teleportation(self):
        if self.x == -50:
            self.x = 1850
            self.y2 = random.randint(100, 500)
            self.y = 0
            self.height = self.y2 - 200
            self.height2 = 600 - self.y2

    def tunumber(self):
        if self.x==400:
            return True
        else:
            return False