
# Импортируем библиотеку pygame
import pygame
from pygame import *
from Player import *
from Security import *
import time


# Объявляем переменные
WIN_WIDTH = 1000  # Ширина создаваемого окна
WIN_HEIGHT = 500  # Высота
DISPLAY = (WIN_WIDTH, WIN_HEIGHT)  # Группируем ширину и высоту в одну переменную
BACKGROUND_COLOR = "#004400"


def main():
    pygame.init()  # Инициация PyGame, обязательная строчка

    screen = pygame.display.set_mode(DISPLAY)  # Создаем окошко
    pygame.display.set_caption("Kate adventure")  # Пишем в шапку
    background_image = pygame.image.load('Images/imgonline-com-ua-Resize-CBt8AmKAPc-AmoyShare.png')


    left = right = False  # по умолчанию - стоим

    sec = Security(600, 300)
    hero = Player(100, 250)  # создаем героя по (x,y) координатам

    timer = pygame.time.Clock()

    entities = pygame.sprite.Group()
    entities.add(hero)
    entities.add(sec)

    pygame.mixer.pre_init(44100, 16, 2, 4096)
    music = pygame.mixer.music.load('Images/casey-edwards-feat (mp3cut.net).mp3')
    pygame.mixer.music.play(-1, 0.0)




    while True:
        screen.blit(background_image, (0, 0)) # Основной цикл программы
        timer.tick(40)
        for e in pygame.event.get():  # Обрабатываем события
            if e.type == QUIT:
                raise SystemExit
            if e.type == KEYDOWN and e.key == K_LEFT:
                left = True
            if e.type == KEYDOWN and e.key == K_RIGHT:
                right = True
            if e.type == KEYUP and e.key == K_RIGHT:
                right = False
            if e.type == KEYUP and e.key == K_LEFT:
                left = False
            if e.type == KEYDOWN and e.key == K_ESCAPE:
                raise SystemExit



        if hero.rect.x >= 700:
            screen.fill((0, 0, 0))
            screen.blit(pygame.image.load('Images/20230221_224141 (1).jpg'), (300, 0))
            pygame.display.update()
            time.sleep(1.5)
            hero.rect.x = 100

        if (((hero.rect.x - sec.rect.x)**2 + (hero.rect.y - sec.rect.y)**2)**0.5 < 60) and (hero.rect.x < sec.rect.x) and (hero.rect.y > sec.rect.y):
            screen.fill((0, 0, 0))
            screen.blit(pygame.image.load('Images/imgonline-com-ua-Resize-QOaXSVgW8gb0.jpg'), (170, 0))
            pygame.display.update()
            time.sleep(1.5)
            hero.rect.x = 100


        hero.update(left, right)  # передвижение
        sec.update()  # передвижение
        entities.draw(screen)
        entities.empty()
        if hero.rect.y > sec.rect.y:
            entities.add(sec)
            entities.add(hero)
        else:
            entities.add(hero)
            entities.add(sec)



        pygame.display.update()  # обновление и вывод всех изменений на экран


if __name__ == "__main__":
    main()
