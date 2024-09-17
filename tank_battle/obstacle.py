import pygame

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((50, 50), pygame.SRCALPHA)
        pygame.draw.circle(self.image, (128, 128, 128), (25, 25), 25)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y