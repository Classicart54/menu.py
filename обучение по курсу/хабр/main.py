import pygame
from pygame import *
from Blocks import Platform
from Player import Player
from Camera import Camera


# Объявляем переменные
WIN_WIDTH = 800  # ширина создаваемого экрана
WIN_HEIGHT = 640  # высота созд. экрана
DISPLAY = (WIN_WIDTH, WIN_HEIGHT)  # группируем ширину и высоту в одну переменную
BACKGROUND_COLOR = "#004400"
# для массива
PLATFORM_WIDTH = 32
PLATFORM_HEIGHT = 32
PLATFORM_COLOR = "#FF6262"



def main():
    pygame.init()  # Инициация PyGame, обязательная строчка
    screen = pygame.display.set_mode(DISPLAY)  # создаем окно
    pygame.display.set_caption("SUper")  # пишем в шапку
    bg = Surface((WIN_WIDTH, WIN_HEIGHT))  # создание видимой поверхности
    # используем как фон
    bg.fill(Color(BACKGROUND_COLOR))  # заливаем цвеетом

    hero = Player(55, 55)  # создаем героя по (x,y) координатам
    left = right = False  # по умолчанию — стоим
    up = False

    # Затем добавим объявление уровня в функцию main

    # А как без него? Под словом «уровень»
    # будем подразумевать ограниченную область
    # виртуального двумерного пространства, заполненную всякой
    # — всячиной, и по которой будет передвигаться наш
    # персонаж.

    # Для построения уровня создадим двумерный массив
    # m на n. Каждая ячейка (m,n) будет представлять из себя
    # прямоугольник. Прямоугольник может в себе что-то
    # содержать, а может и быть пустым. Мы в прямоугольниках
    # будем рисовать платформы.

    entities = pygame.sprite.Group()  # все объекты
    # Группа спрайтов entities будем использовать для отображения всех элементов этой группы.

    platforms = []  # то, во что мы будем врезаться
    # Массив platforms будем использовать для проверки на пересечение с платформой.
    entities.add(hero)

    level = [
        "----------------------------------",
        "-                                -",
        "-                       --       -",
        "-                                -",
        "-            --                  -",
        "-                                -",
        "--                               -",
        "-                                -",
        "-                   ----     --- -",
        "-                                -",
        "--                               -",
        "-                                -",
        "-                            --- -",
        "-                                -",
        "-                                -",
        "-      ---                       -",
        "-                                -",
        "-   -------         ----         -",
        "-                                -",
        "-                         -      -",
        "-                            --  -",
        "-                                -",
        "-                                -",
        "----------------------------------"]
    timer = pygame.time.Clock()

    def camera_configure(camera, target_rect):
        l, t, _, _ = target_rect
        _, _, w, h = camera
        l, t = -l + WIN_WIDTH / 2, -t + WIN_HEIGHT / 2

        l = min(0, l)  # Не движемся дальше левой границы
        l = max(-(camera.width - WIN_WIDTH), l)  # Не движемся дальше правой границы
        t = max(-(camera.height - WIN_HEIGHT), t)  # Не движемся дальше нижней границы
        t = min(0, t)  # Не движемся дальше верхней границы

        return Rect(l, t, w, h)

    total_level_width = len(level[0])*PLATFORM_WIDTH  # высчитываем фактическую ширину уровня
    total_level_height = len(level)*PLATFORM_HEIGHT  # высоту

    camera = Camera(camera_configure, total_level_width, total_level_height)


    running = True
    while running:
        timer.tick(60)
        screen.blit(bg, (0, 0))
        for e in pygame.event.get():  # обрабатываем события
            if e.type == QUIT:
                raise SystemExit("QUIT")
            if e.type == KEYDOWN and e.key == K_LEFT:
                left = True
            if e.type == KEYDOWN and e.key == K_RIGHT:
                right = True
            if e.type == KEYUP and e.key == K_LEFT:
                left = False
            if e.type == KEYUP and e.key == K_RIGHT:
                right = False
            if e.type == KEYDOWN and e.key == K_UP:
                up = True
            if e.type == KEYUP and e.key == K_UP:
                up = False
        x = y = 0  # координаты
        for row in level:  # вся строка в массиве level. мы через массив отображаем платформы
            for col in row:  # каждый символ
                if col == "-":
                    pf = Platform(x, y)
                    entities.add(pf)
                    platforms.append(pf)
                    # Т.е. создаём экземплр класса Platform, добавляем
                    # его в группу спрайтов entities и массив platforms.
                    # В entities, чтобы для каждого блока не писать логику
                    # отображения. В platforms добавили, чтобы потом проверить
                    # массив блоков на пересечение с игроком.

                x += PLATFORM_WIDTH  # блоки платформы ставятся на ширине блоков
            y += PLATFORM_HEIGHT  # то же самое и с высотой
            x = 0

        hero.update(left, right, up, platforms)  # передвижение
        camera.update(hero)  # центр. камеру относительно перса
        for e in entities:
            screen.blit(e.image, camera.apply(e))

        pygame.display.update()


            # Т.е. Мы перебираем двумерный массив level,
            # и, если находим символ «-», то по координатам
            # (x * PLATFORM_WIDTH, y * PLATFORM_HEIGHT), где
            # x,y — индекс в массиве level

if __name__ == "__main__":
    main()
