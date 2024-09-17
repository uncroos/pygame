import pygame
import sys
import random
from tank import Tank
from bullet import Bullet
from obstacle import Obstacle

# 초기화
pygame.init()

# 화면 설정
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tank Battle")

# 색상
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# 탱크 생성
tank1 = Tank(100, 300, (0, 0, 255))  # 파란색 탱크
tank2 = Tank(700, 300, (0, 255, 0))  # 초록색 탱크

# 총알 그룹
bullets = pygame.sprite.Group()

# 장애물 그룹
obstacles = pygame.sprite.Group()

# 장애물 생성
for _ in range(5):
    x = random.randint(0, WIDTH)
    y = random.randint(0, HEIGHT)
    obstacle = Obstacle(x, y)
    obstacles.add(obstacle)
    
# 폰트
font = pygame.font.Font(None, 36)

# 게임 오버 함수
def game_over(winner):
    screen.fill(BLACK)
    game_over_text = font.render(f"Game Over! {winner} Wins!", True, WHITE)
    restart_text = font.render("Press R to Restart", True, WHITE)
    screen.blit(game_over_text, (WIDTH//2 - game_over_text.get_width()//2, HEIGHT//2 - 50))
    screen.blit(restart_text, (WIDTH//2 - restart_text.get_width()//2, HEIGHT//2 + 50))
    pygame.display.flip()
    
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    return True  # 재시작
    return False

# 게임 루프
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
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
        
        # 장애물과 총알 충돌
        if pygame.sprite.spritecollide(bullet, obstacles, False):
            bullet.kill()

    # 탱크와 장애물 충돌
    pygame.sprite.spritecollide(tank1, obstacles, False)
    pygame.sprite.spritecollide(tank2, obstacles, False)

    # 화면 그리기
    screen.fill(WHITE)
    tank1.draw(screen)
    tank2.draw(screen)
    bullets.draw(screen)
    obstacles.draw(screen)

    # 체력 표시
    health1 = font.render(f"Player 1: {tank1.health}", True, BLACK)
    health2 = font.render(f"Player 2: {tank2.health}", True, BLACK)
    screen.blit(health1, (10, 10))
    screen.blit(health2, (WIDTH - 150, 10))

    pygame.display.flip()
    clock.tick(60)

    # 게임 오버 체크
    if tank1.health <= 0:
        if game_over("Player 2"):
            # 게임 리셋
            tank1.reset(100, 300)
            tank2.reset(700, 300)
            bullets.empty()
        else:
            running = False
    elif tank2.health <= 0:
        if game_over("Player 1"):
            # 게임 리셋
            tank1.reset(100, 300)
            tank2.reset(700, 300)
            bullets.empty()
        else:
            running = False

pygame.quit()
sys.exit()