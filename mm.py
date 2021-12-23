import pygame

pygame.init()


def menu():
    a=0
    screenX=1920
    screenY=1080
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

    play_file = 'графика/кнопки/play.png'
    exit_file = 'графика/кнопки/exit.png'
    help_file = "графика/кнопки/about.png"
    bg_file = "графика/bg/а.png"

    bg = pygame.image.load(bg_file)
    exitt = pygame.image.load(exit_file)
    play = pygame.image.load(play_file)
    myHelp = pygame.image.load(help_file)
    screen.blit(bg, [0, 0])
    screen.blit(play, [screenX / 2 - 90, screenY / 2 - 300])
    screen.blit(myHelp, [screenX / 2 - 90, screenY / 2 - 200])
    screen.blit(exitt, [screenX / 2 - 90, screenY / 2 - 100])


    running = True
    pygame.display.update()
    while running:
        for event in pygame.event.get():
            (x, y) = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if screenX / 2 - 100 <= x <= screenX / 2 + 100 and screenY / 2 - 300 - 25 <= y <= screenY / 2 + 25 - 300:
                    a = 'game'
                    running = False
                if screenX / 2 - 100 <= x <= screenX / 2 + 100 and screenY / 2 - 200 - 25 <= y <= screenY / 2 + 25 - 200:
                    a = 'help'
                    running = False
                if screenX / 2 - 100 <= x <= screenX / 2 + 100 and screenY / 2 - 100 - 25 <= y <= screenY / 2 - 100 + 25:
                    a = 'exit'
                    running = False

    return(a)
