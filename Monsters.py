import pygame as pg
import main
from pygame import *

mob_file = "графика/monsters/11.png"


class Monster(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pg.transform.scale(pg.image.load(mob_file), (240, 240))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.init_trajectory()

        self.hp = 3
        self.damage_default = 0

    def update(self):
        new_x = self.rect.x + self.speed

        if new_x < self.trajectory_start:
            delta = self.trajectory_start - new_x
            self.speed *= -1
        elif new_x > self.trajectory_end:
            delta = self.trajectory_end - new_x
            self.speed *= -1
        else:
            delta = self.speed

        self.rect.x += delta

    def init_trajectory(self):
        self.trajectory_length = 100
        self.trajectory_start = self.rect.x - self.trajectory_length
        self.trajectory_end = self.rect.x + self.trajectory_length
        self.speed = 5

        print(self.trajectory_start, self.trajectory_end)
