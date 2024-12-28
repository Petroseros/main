import pygame.draw


class Bird:
    def __init__(self):
        self.x = 400
        self.y = 280
        self.width = 90
        self.height = 64
        self.speed = 1
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.animation_frames = 10
        self.images = [pygame.image.load(f'flap{i}.png') for i in range(1, 4)]
        self.imaged = 0

    def display(self, screen):
        self.animation_frames -= 1
        if self.animation_frames == 0:
            self.animation_frames = 10
            self.imaged += 1
        if self.imaged == 3:
              self.imaged = 0
        screen.blit(self.images[self.imaged], self.rect)

    def move(self):
        self.rect.y += self.speed
        self.speed += 1

    def jump(self):
        self.speed = -15

    def death(self, tubes):
        for tube in tubes:
            if self.rect.colliderect(tube.rect) or self.rect.y <= 0 or self.rect.y >= 560:
                return True
        return False
