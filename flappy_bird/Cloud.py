import pygame.draw

import random


class Cloud:
    def __init__(self,x):
        self.x = x
        self.y = 50
        self.width = 100
        self.speed = 5
        self.height = 75

    def display(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), (self.x, self.y, self.width, self.height))

    def move(self):
        self.x -= self.speed

    def teleportation(self):
        if self.x == -50:
            self.x = 1800
            self.y = random.randint(30, 100)
            self.width = random.randint(50, 200)
            self.height = random.randint(30, 130)