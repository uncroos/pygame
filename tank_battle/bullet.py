import pygame
import math

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, angle):
        super().__init__()
        self.image = pygame.Surface((5, 5))
        self.image.fill((255, 0, 0))  # 빨간색 총알
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = 7
        self.angle = angle
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update(self):
        self.x += self.speed * math.cos(math.radians(self.angle))
        self.y -= self.speed * math.sin(math.radians(self.angle))
        self.rect.x = int(self.x)
        self.rect.y = int(self.y)
        
        # 화면 밖으로 나가면 제거
        if not pygame.display.get_surface().get_rect().collidepoint(self.rect.center):
            self.kill()