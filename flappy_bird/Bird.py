import pygame.draw

class Bird:
    def __init__(self):
        self.x = 400
        self.y = 280
        self.side = 40
        self.speed = 1

    def display(self, screen):
        pygame.draw.rect(screen, (255, 255, 0), (self.x, self.y, self.side, self.side))

    def move(self):
        self.y += self.speed
        self.speed += 1

    def jump(self):
        self.speed = -15