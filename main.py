import pygame as pg
from player import Player
from Gem import Gem
import random
from Monsters import Monster

FPS = 60
level = 0
col = 0
pg.display.set_icon(pg.image.load("icon.jpg"))
backmenu_file = 'графика/bg/background-menu.png'
backmenu = pg.image.load(backmenu_file)

def make_gems():
    global count
    gems = pg.sprite.Group()
    count = random.randint(1, 3)  # определение количества кристаллов
    for _ in range(count):
        gems.add(Gem())

    return gems

def draw_score(score, screen):
    f = pg.font.SysFont('arial', 30)
    d = f.render(str(score), True, (255,) * 3)
    screen.blit(d, (0, 0))

def main():
    global level
    pg.init()

    BG = pg.transform.scale(pg.image.load("графика/bg/1.png"), (1920, 1080))
    gems = make_gems()
    screen = pg.display.set_mode((0, 0), pg.FULLSCREEN)
    player = Player(screen)
    sprites = pg.sprite.Group()
    sprites.add(player)
    tick = pg.time.Clock().tick

    monster3 = Monster(random.randint(500, 700), random.randint(200, 900))
    monster2 = Monster(random.randint(300, 1700), random.randint(200, 900))
    monster4 = Monster(random.randint(300, 1700), random.randint(200, 900))

    score = 0
    col = 0

    running = True
    while running:
        tick(FPS)
        screen.blit(BG, (0, 0))
        for event in pg.event.get():
            if pg.key.get_pressed()[pg.K_ESCAPE]:
                running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    player.shoot()

        # Смена уровня

        if pg.sprite.spritecollide(player, gems, dokill=True):
            score += 1
            col += 1

        if 1500 <= player.rect.x < 1920 and 900 <= player.rect.y < 1080 and level == 0 and col == count:
            BG = pg.transform.scale(pg.image.load("графика/bg/2.png"), (1920, 1080))
            level = 1  # если 2й уровень, то ставим левел на 1

            monster3 = Monster(random.randint(500, 700), random.randint(200, 900))
            monster2 = Monster(random.randint(300, 1700), random.randint(200, 900))
            monster4 = Monster(random.randint(300, 1700), random.randint(200, 900))
            score += col
            score -= col
            col = 0
            make_gems()
            gems = make_gems()
            gems.update()
            sprites.update()
            gems.draw(screen)
            player.rect.x = 1700
            player.rect.y = 50

        if 300 <= player.rect.x < 500 and 550 <= player.rect.y < 750 and level == 1 and col == count:  # если такие-то координаты и левел равен 1(если локация 2)
            BG = pg.transform.scale(pg.image.load("графика/bg/3.png"), (1920, 1080))
            level = 2  # если 3й уровень, то меняем левел на 2
            score += col
            score -= col
            col = 0
            monster3 = Monster(random.randint(500, 700), random.randint(200, 900))
            monster2 = Monster(random.randint(300, 1700), random.randint(200, 900))
            monster4 = Monster(random.randint(300, 1700), random.randint(200, 900))

            make_gems()
            gems = make_gems()
            gems.update()
            sprites.update()
            gems.draw(screen)

        if 1920-200 <= player.rect.x > 1920-200 and 740 <= player.rect.y < 840 and level == 2 and col == count:  # если такие-то координаты и левел равен 3(если локация 3)
            BG = pg.transform.scale(pg.image.load("графика/bg/4.png"), (1920, 1080))
            level = 3  # если 3й уровень, то меняем левел на 2
            monster3 = Monster(random.randint(500, 700), random.randint(200, 900))
            monster2 = Monster(random.randint(300, 1700), random.randint(200, 900))
            monster4 = Monster(random.randint(300, 1700), random.randint(200, 900))
            score += col
            score -= col
            col = 0
            make_gems()
            gems = make_gems()
            gems.update()
            sprites.update()
            gems.draw(screen)

            player.rect.x = 100
            player.rect.y = 800

        gems.update()
        sprites.update()
        sprites.draw(screen)
        gems.draw(screen)

        monster2.update()
        screen.blit(monster2.image, monster2.rect)
        monster3.update()
        screen.blit(monster3.image, monster3.rect)
        monster4.update()
        screen.blit(monster4.image, monster4.rect)
        draw_score(score, screen)
        pg.display.update()

    pg.quit()

if __name__ == '__main__':
    main()


# Сделать:
# 1. Врагов. Чтобы при попадании персонажа на уровень, они атаковали его. Ближним боем. Чтобы они умирали.
# 2. Алмазы. Счетчик алмазов. Чтобы собирать алмазы. +
# 3. Менюшка. Переход по кнопкам. +
# 4. Всплывающий окна с текстом(сказка про сюжет).
# 5. возможно. Лечащие предметы.
# 6. Дорисовать все необходимое.
