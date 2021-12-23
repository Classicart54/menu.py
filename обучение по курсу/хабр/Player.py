import self as self
from pygame import *

MOVE_SPEED = 20
WIDTH = 22
HEIGHT = 32
COLOR = "#888888"
JUMP_POWER = 15
GRAVITY = 0.5  # сила, которая будет тянуть нас вниз


class Player(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.xvel = 0  # скорость перемещения. 0 - стоять на месте
        self.startX = x  # начальная позиция X, пригодится, когда переигрывать будем
        self.startY = y
        self.image = Surface((WIDTH, HEIGHT))
        self.image.fill(Color(COLOR))
        self.rect = Rect(x, y, WIDTH, HEIGHT)  # прямоугольный объект
        self.yvel = 0  # скорость вертикального перемещения
        self.onGround = False  # На земле ли я?

    def update(self, left, right, up, platforms):
        if up:
            if self.onGround:  # прыгаем, только когда можем оттолкнуться от земли
                self.yvel = -JUMP_POWER
        self.xvel = 0
        if left:
            self.xvel = -MOVE_SPEED  # лево  = x - n

        if right:
            self.xvel = MOVE_SPEED  # право = x + n

        if not(left or right):  # стоим, когда нет указаний идти
            self.xvel = 0

        if not self.onGround:  # если не на земле, то + гравитация
            self.yvel += GRAVITY

        self.onGround = False  # мы не знаем, когда мы на земле

        self.rect.y += self.yvel
        self.collide(0, self.yvel, platforms)
        self.rect.x += self.xvel  # переносим свои положение на xvel
        self.collide(self.xvel, 0, platforms)

    def collide(self, xvel, yvel, platforms):
        for p in platforms:
            if sprite.collide_rect(self, p):  # если есть пересечение платформы с игроком
                # т.е. тут проходит проверка. если персонаж пришел к концу карты, то выполняются след. условия
                if xvel > 0:                        # если движется вправо
                    self.rect.right = p.rect.left   # то не движется вправо

                if xvel < 0:                        # если движется влево
                    self.rect.left = p.rect.right   # то не движется влево

                if yvel > 0:                        # если падает вниз
                    self.rect.bottom = p.rect.top   # то не падает вниз
                    self.onGround = True  # "активируем твердость платформ"
                    self.yvel = 0

                if yvel < 0:                        # если движется вверх
                    self.rect.top = p.rect.bottom   # то не движется вверх
                    self.yvel = 0                   # и энергия прыжка пропадает
# В этом методе происходит проверка
# на пересечение координат героя и платформ,
# если таковое имеется, то выше описанной логике
# происходит действие.

