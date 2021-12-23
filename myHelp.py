import pygame
pygame.init()
from pygame import *
from pygame.color import THECOLORS
def helpGAME():

    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    BG = pygame.transform.scale(pygame.image.load("графика/bg/myyhelp.png"), (1920, 1080))
    screen.blit(BG, [0, 0])
    pygame.display.flip()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

