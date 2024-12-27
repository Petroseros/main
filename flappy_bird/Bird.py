import pygame.draw

class Bird:
    def __init__(self):
        self.x = 400
        self.y = 280
        self.side = 40
        self.speed = 1
        self.rect = pygame.Rect(self.x, self.y, self.side, self.side)

    def display(self, screen):
        pygame.draw.rect(screen, (255, 255, 0), self.rect)

    def move(self):
        self.rect.y += self.speed
        self.speed += 1

    def jump(self):
        self.speed = -15

    def death(self,tubes):
        for tube in tubes:
            if self.rect.colliderect(tube.rect) or self.rect.y <= 0 or self.rect.y >= 560:
                return True
        return False