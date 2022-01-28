import sys
import pygame
from settings import *
from level import Level

pygame.init()
screen_width = 1280
screen_height = 700
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
level = Level(level_map, screen)
icon = pygame.image.load('graphics/icon/icon.png')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill('black')
    level.run()

    pygame.display.set_caption('Platformer by Viktor')
    pygame.display.set_icon(icon)
    pygame.display.update()
    clock.tick(60)
