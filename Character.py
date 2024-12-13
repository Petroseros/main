import pygame.draw


class Character:
    def __init__(self):
        self.x = 475
        self.y = 275
        self.side = 50
        self.speedx = 1
        self.speedy = 1

    def display(self, screen):
        pygame.draw.rect(screen, (225, 225, 225), (self.x, self.y, self.side, self.side))

    def move(self):
        self.y += self.speedy
        self.speedy += 1

    def jump(self):
        self.speedy = -10