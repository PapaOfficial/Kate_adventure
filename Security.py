
from pygame import *

MOVE_SPEED = 4
WIDTH = 50
HEIGHT = 100
COLOR =  "#888888"


class Security(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.xvel = 6  # скорость перемещения. 0 - стоять на месте
        self.yvel = 6
        self.startX = x # Начальная позиция Х, пригодится когда будем переигрывать уровень
        self.startY = y
        self.image = image.load('Images/1679999257901.png')
        self.rect = Rect(x, y, WIDTH, HEIGHT) # прямоугольный объект

    def update(self):
        if self.rect.x >= 650:
            self.xvel = -6
            self.yvel = -6

        if self.rect.x <= 450:
            self.xvel = 6
            self.yvel = 6

        self.rect.x += self.xvel # переносим свои положение на xvel
        self.rect.y += self.yvel  # переносим свои положение на xvel

