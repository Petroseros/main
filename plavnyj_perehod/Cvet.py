import pygame.draw
R = 255
G = 255
B = 255
class Cvet:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.height = 50
        self.width = 1
        self.speed = 1

    def display(self, screen):
        pygame.draw.rect(screen, (R, G, B), (self.x, self.y, self.width, self.height))

    def move(self, G=255, B=255, R=255):
        self.x += self.speed
        R -= 1
        G -= 1
        B -= 1