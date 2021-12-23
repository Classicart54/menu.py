import pygame
from pygame.color import THECOLORS

pygame.init()

delay = 100
interval = 50

screenX = 900
screenY = 600
screen = pygame.display.set_mode([screenX, screenY])
xr = 0
yr = 200

xr1 = 870
yr1 = 200

width = 30
heigth = 150
step = 10  # Шаг ракетки. При каждом шаге ракетка перемещается на 10 пикселей

pygame.key.set_repeat(delay, interval)

pygame.draw.rect(screen, THECOLORS['brown'], [xr, yr, width, heigth], 0)

pygame.draw.rect(screen, THECOLORS['brown'], [xr1, yr1, width, heigth], 0)

running = True
while running:
    screen.fill(THECOLORS['white'])  # Стираем все изображения
    for event in pygame.event.get():  # Закрываем окно, если необходимо
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:  # Движение ракетки
            if event.key == pygame.K_UP:
                yr = yr - step  # Перемещаемся на шаг вверх​
            elif event.key == pygame.K_DOWN:
                yr = yr + step  # И так далее​
            elif event.key == pygame.K_LEFT:
                xr = xr - step
            elif event.key == pygame.K_RIGHT:
                xr = xr + step
    for event in pygame.event.get():  # Закрываем окно, если необходимо
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:  # Движение ракетки
            if event.key == pygame.K_w:
                yr1 = yr1 - step  # Перемещаемся на шаг вверх
            elif event.key == pygame.K_s:
                yr1 = yr1 + step  # И так далее
            elif event.key == pygame.K_a:
                xr1 = xr1 - step
            elif event.key == pygame.K_d:
                xr1 = xr1 + step


    pygame.draw.rect(screen, THECOLORS['brown'], [xr, yr, width, heigth], 0)
    pygame.draw.rect(screen, THECOLORS['brown'], [xr1, yr1, width, heigth], 0)
    pygame.display.flip()
pygame.quit()
