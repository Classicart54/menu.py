import pygame

pygame.init()

W = 600
H = 400

sc = pygame.display.set_mode((W, H))
pygame.display.set_caption("События от мыши")

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

FPS = 60
clock = pygame.time.Clock()

flStartDraw = False
sp = ep = None

sc.fill(WHITE)
pygame.display.update()


while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            flStartDraw = True
            sp = event.pos
        elif event.type == pygame.MOUSEMOTION:
            if flStartDraw:
                pos = event.pos

                width = pos[0] - sp[0]
                height = pos[1] - sp[1]

                sc.fill(WHITE)
                pygame.draw.rect(sc, RED, (sp[0], sp[1], width, height))
                pygame.display.update()
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            flStartDraw = False

    clock.tick(FPS)



    clock.tick(FPS)









while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()


    clock.tick(FPS)









