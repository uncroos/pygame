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