import self as self
from pygame import *

WIN_WIDTH = 800  # ширина создаваемого экрана
WIN_HEIGHT = 640  # высота созд. экрана


class Camera(object):
    def __init__(self, camera_func, width, height):
        self.camera_func = camera_func
        self.state = Rect(0, 0, width, height)

    def apply(self, target):
        return target.rect.move(self.state.topleft)

    def update(self, target):
        self.state = self.camera_func(self.state, target.rect)




