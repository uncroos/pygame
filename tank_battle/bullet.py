import pygame
import sys
from tank import Tank
from bullet import Bullet

# 초기화
pygame.init()

# 화면 설정
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tank Battle")

# 색상
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# 탱크 생성
tank1 = Tank(100, 300, "assets/tank1.png")
tank2 = Tank(700, 300, "assets/tank2.png")

# 총알 그룹
bullets = pygame.sprite.Group()

# 게임 루프
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        # 키 입력 처리
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullets.add(tank1.shoot())
            if event.key == pygame.K_RETURN:
                bullets.add(tank2.shoot())

    # 탱크 이동
    keys = pygame.key.get_pressed()
    tank1.move(keys[pygame.K_a], keys[pygame.K_d], keys[pygame.K_w], keys[pygame.K_s])
    tank2.move(keys[pygame.K_LEFT], keys[pygame.K_RIGHT], keys[pygame.K_UP], keys[pygame.K_DOWN])

    # 총알 업데이트
    bullets.update()

    # 충돌 검사
    for bullet in bullets:
        if pygame.sprite.collide_rect(bullet, tank1):
            tank1.hit()
            bullet.kill()
        if pygame.sprite.collide_rect(bullet, tank2):
            tank2.hit()
            bullet.kill()

    # 화면 그리기
    screen.fill(WHITE)
    tank1.draw(screen)
    tank2.draw(screen)
    bullets.draw(screen)

    # 체력 표시
    font = pygame.font.Font(None, 36)
    health1 = font.render(f"Player 1: {tank1.health}", True, BLACK)
    health2 = font.render(f"Player 2: {tank2.health}", True, BLACK)
    screen.blit(health1, (10, 10))
    screen.blit(health2, (WIDTH - 150, 10))

    pygame.display.flip()
    clock.tick(60)