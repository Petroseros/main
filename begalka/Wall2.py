import pygame.draw

class Wall2:
    def __init__(self):
        self.x = 849
        self.y = 970
        self.height = 30
        self.width = 150
        self.speed = 1
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def display(self, screen):
        pygame.draw.rect(screen, (133,133,133), self.rect)

    def move(self):
        self.rect.x -= self.speed
        if self.rect.x == 850:
            self.speed = self.speed * -1
        if self.rect.x == 0:
            self.speed = self.speed * -1