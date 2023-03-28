
from pygame import *

MOVE_SPEED = 7
WIDTH = 50
HEIGHT = 100
COLOR = "#888888"


class Player(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.xvel = 0  # скорость перемещения. 0 - стоять на месте
        self.startX = x # Начальная позиция Х, пригодится когда будем переигрывать уровень
        self.startY = y
        self.image = image.load('Images/1679998458192.png')
        self.rect = Rect(x, y, WIDTH, HEIGHT) # прямоугольный объект

    def update(self,  left, right):
        if left:
            self.xvel = -MOVE_SPEED # Лево = x- n
            if self.rect.x <= 50:
                self.xvel = 0

        if right:
            self.xvel = MOVE_SPEED # Право = x + n

        if not(left or right): # стоим, когда нет указаний идти
            self.xvel = 0

        self.rect.x += self.xvel # переносим свои положение на xvel

