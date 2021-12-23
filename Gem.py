import pygame as pg
from random import randint


class Gem(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.transform.scale(pg.image.load("графика/geme.png"), (70, 52))
        self.rect = self.image.get_rect()
        self.rect.x = randint(0, 1920 - self.rect.width - 100)
        self.rect.y = randint(0, 1080 - self.rect.height - 100)


