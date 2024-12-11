import pygame.draw

class Tube:
    def __init__(self):
        self.x = 1010
        self.y = 400
        self.x2 = 1010
        self.y2 = 0
        self.width = 50
        self.height = 200
        self.speed = 10
    def display(self, screen):
        pygame.draw.rect(screen, (225, 225, 225), (self.x, self.y, self.width, self.height))
        pygame.draw.rect(screen, (225, 225, 225), (self.x2, self.y2, self.width, self.height))
    def move(self):
        self.x -= self.speed
        self.x2 -= self.speed