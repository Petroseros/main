import pygame.draw
class Chelovechek:
    def __init__(self):
        self.x = 525
        self.y = 525
        self.size = 50
        self.speed = 1

    def display(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), (self.x, self.y, self.size, self.size))

    def up(self):
        self.y -= self.speed
    def down(self):
        self.y += self.speed
    def left(self):
        self.x -= self.speed
    def right(self):
        self.x += self.speed