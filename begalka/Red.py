import pygame.draw

class Red:
    def __init__(self):
        self.x = 800
        self.y = 800
        self.size = 50
        self.speed = 0.4
        self.rect = pygame.Rect(self.x, self.y, self.size, self.size)

    def display(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), self.rect)

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rect.x -= self.speed
        if keys[pygame.K_d]:
            self.rect.x += self.speed
        if keys[pygame.K_w]:
            self.rect.y -= self.speed
        if keys[pygame.K_s]:
            self.rect.y += self.speed

        if self.rect.y <= 0:
            self.rect.y = 0.1
        if self.rect.y >= 950:
            self.rect.y = 949.9
        if self.rect.x <= 0:
            self.rect.x = 0.1
        if self.rect.x >= 950:
            self.rect.x = 949.9

    def tele(self,wall1,wall2):
        if self.rect.colliderect(wall1.rect):
            self.rect.x = wall2.rect.x
            self.rect.y = wall2.rect.y - 30
        if wall1.rect.colliderect(wall2.rect):
            self.rect.x = wall1.rect.x
            self.rect.y = wall1.rect.y + 30