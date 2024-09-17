import pygame
from bullet import Bullet

class Tank(pygame.sprite.Sprite):
    def __init__(self, x, y, color):
        super().__init__()
        self.original_image = pygame.Surface((40, 40))
        self.original_image.fill(color)
        self.image = self.original_image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 5
        self.health = 100
        self.angle = 0

    def move(self, left, right, up, down):
        dx, dy = 0, 0
        if left:
            dx -= self.speed
            self.angle = 180
        if right:
            dx += self.speed
            self.angle = 0
        if up:
            dy -= self.speed
            self.angle = 90
        if down:
            dy += self.speed
            self.angle = 270

        self.rect.x += dx
        self.rect.y += dy

        # 회전
        self.image = pygame.transform.rotate(self.original_image, self.angle)
        self.rect = self.image.get_rect(center=self.rect.center)

        # 화면 경계 처리
        self.rect.clamp_ip(pygame.display.get_surface().get_rect())

    def shoot(self):
        bullet_x = self.rect.centerx
        bullet_y = self.rect.centery
        return Bullet(bullet_x, bullet_y, self.angle)

    def hit(self):
        self.health -= 10
        if self.health <= 0:
            self.kill()

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def reset(self, x, y):
        self.rect.x = x
        self.rect.y = y
        self.health = 100
        self.angle = 0
        self.image = self.original_image