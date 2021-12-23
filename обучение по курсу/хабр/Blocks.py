import self as self
from pygame import *


PLATFORM_WIDTH = 32
PLATFORM_HEIGHT = 32
PLATFORM_COLOR = "#FF6262"

class Platform(sprite.Sprite): # создаем класс, наследуясь от pg.sprite.Sprite
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))  # делаем коллизию. (твердость)
        self.image = image.load("graphics/platform.png")  # придаем ей цвет
        self.rect = Rect(x, y, PLATFORM_WIDTH, PLATFORM_HEIGHT)  # рисуем саму платформу


