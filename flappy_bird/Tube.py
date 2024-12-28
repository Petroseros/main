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
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.rect2 = pygame.Rect(self.x, self.y2, self.width, self.height2)

    def display(self, screen):
        pygame.draw.rect(screen, (33, 128, 61), self.rect)
        pygame.draw.rect(screen, (33, 128, 61), self.rect2)

    def move(self):
        self.rect.x -= self.speed
        self.rect2.x -= self.speed

    def teleportation(self):
        if self.rect.x == -50:
            self.rect.x = 1850
            self.rect2.x = 1850
            self.rect2.y = random.randint(100, 500)
            self.rect.y = 0
            self.rect.height = self.rect2.y - 200
            self.rect2.height = 600 - self.rect2.y

    def tunumber(self):
        if self.rect.x == 350:
            return True
        else:
            return False