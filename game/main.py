import os
import pygame
#########################################

#pygame 기본 초기화
pygame.init()

#화면 크기 설정
screen_width = 480 #가로
screen_height = 632.18 #세로
screen = pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀 설정
pygame.display.set_caption("고전 픽셀 게임")

#FPS(Frame Per Second) 설정
clock = pygame.time.Clock()

#게임 초기화(배경화며나, 이미지, 좌표, 속도 등등)
current_path = os.path.dirname(__file__) #현재 파일의 경로
image_path = os.path.join(current_path, "images")

#배경 이미지
background = pygame.image.load(os.path.join(image_path, "background.png"))

#스테이지 이지미
stage = pygame.image.load(os.path.join(image_path, "stage.png"))
stage_size = stage.get_rect().size
stage_height = stage_size[1]