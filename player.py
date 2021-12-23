import self as self
import pygame as pg
from pygame import *
from Monsters import Monster
import random
pg.font.init()
import pyganim
from pygame.color import THECOLORS

count = 0
f = pg.font.Font(None, 20)
COMMON_SPEED = 15
SCREEN_HEIGHT = 1080
SCREEN_WIDTH = 1920
HOR, VERT = 50, 50
COLOR = "#888888"
HP = 10

l, r = HOR, SCREEN_WIDTH - HOR
u, d = VERT, SCREEN_HEIGHT - VERT


walkRight = {"step": 0,
             "anim": ['графика/anim/1.png',
                      'графика/anim/2.png',
                      'графика/anim/3.png',
                      'графика/anim/4.png',
                      'графика/anim/5.png',
                      'графика/anim/6.png',
                      'графика/anim/7.png', ]}

walkLeft = {"step": 0,
            "anim": ['графика/anim/left/1.png',
                     'графика/anim/left/2.png',
                     'графика/anim/left/3.png',
                     'графика/anim/left/4.png',
                     'графика/anim/left/5.png',
                     'графика/anim/left/6.png',
                     'графика/anim/left/7.png', ]}

bullets = []


class Player(pg.sprite.Sprite):
    def __init__(self, screen):
        super().__init__()
        self.image = pg.transform.scale(pg.image.load("графика/drag.png"), (100, 83))  # загрузка изобраения персонажа
        self.rect = self.image.get_rect()
        self.screen = screen
        self.direction = "right"
        self.hit = 1 # количество отнимаемых хп у монстра от одной пульки


    # СТРЕЛЬБА. Характеристики стрельбы.

    def shoot(self):
        if self.direction == "right":
            bullets.append({
                "x": self.rect.x + self.rect.width + 7,
                "y": self.rect.y + 37,
                "direction": "right",
            })
        elif self.direction == "left":
            bullets.append({
                "x": self.rect.x - 7,
                "y": self.rect.y + 37,
                "direction": "left",
            })

    # def gems(self):
    #     global flag, count, number
    #     # КРИСТАЛЛЫ
    #     flag = True
    #     xui = BIGXUI
    #     number = random.randint(3, 6)
    #       print(XUI.size * 100)
    #
    #     for i in range(number):
    #         if flag == True:
    #             x_cris = random.randint(100, 1800)
    #             y_cris = random.randint(100, 900)
    #             self.screen.blit(pg.transform.scale(pg.image.load("графика/geme.png"), (70, 52)), [x_cris, y_cris])
    #             if x_cris < self.rect.x < x_cris + 70 and y_cris < self.rect.y < y_cris + 52 or x_cris + 70 < self.rect.x < x_cris and y_cris + 52 < self.rect.y < y_cris:
    #                 count += 1
    #                 flag = False
    #                 print(x_cris, y_cris, self.rect.x, self.rect.y)
    #         text = f.render(str(count), True, (255, 255, 255))
    #         self.screen.blit(text, [10, 10])



    def update(self):
        key = pg.key.get_pressed()
        left = key[pg.K_a]
        right = key[pg.K_d]
        speedy = 0
        col = 0
        speedx = 0
        keystate = pg.key.get_pressed()

        # движение персонажа

        if keystate[pg.K_w]:
            speedy = -COMMON_SPEED
        elif keystate[pg.K_s]:
            speedy = COMMON_SPEED

        self.rect.y += speedy

        if self.rect.bottom > d:
            self.rect.bottom = d
        if self.rect.top < u:
            self.rect.top = u

        if keystate[pg.K_a]:
            speedx = -COMMON_SPEED
        elif keystate[pg.K_d]:
            speedx = COMMON_SPEED

        self.rect.x += speedx

        if self.rect.left < l:
            self.rect.left = l
        if self.rect.right > r:
            self.rect.right = r

        # анимации на каждое движение

        if keystate[pg.K_a]:
            self.direction = "left"
            self.xvel = -COMMON_SPEED  # Лево = x- n

            if walkLeft["step"] == len(walkLeft["anim"]):
                walkLeft["step"] = 0
            self.image = pg.transform.scale(pg.image.load(walkLeft["anim"][walkLeft["step"]]), (100, 83))
            walkLeft["step"] += 1

        elif keystate[pg.K_d]:
            self.direction = "right"
            self.xvel = COMMON_SPEED  # Право = x + n
            self.image.fill(Color(COLOR))

            if walkRight["step"] == len(walkRight["anim"]):
                walkRight["step"] = 0
            self.image = pg.transform.scale(pg.image.load(walkRight["anim"][walkRight["step"]]), (100, 83))
            walkRight["step"] += 1



        for bullet in bullets:
            self.screen.blit(pg.transform.scale(pg.image.load("графика/bullet1.png"), (9, 7)),
                             [bullet["x"], bullet["y"]])
        # Bullets logic
        for bullet in bullets:
            if bullet["direction"] == "right":
                if bullet["x"] + 5 < SCREEN_WIDTH:
                    bullet["x"] += 30
                else:
                    bullets.remove(bullet)
            elif bullet["direction"] == "left":
                if bullet["x"] > 0:
                    bullet["x"] -= 30
                else:
                    bullets.remove(bullet)










