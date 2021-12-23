import pygame
pygame.init()

sc = pygame.display.set_mode((600, 400), pygame.RESIZABLE)
pygame.display.set_caption("First") # свое название
# pygame.display.set_icon((pygame.image.load("name.bmp"))) # своя иконка игры
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)



pygame.draw.rect(sc, WHITE,  (10, 10, 50, 100), 2) # x, y, width, height

pygame.draw.line(sc, GREEN, (200, 20), (350, 50), 5)

pygame.draw.lines(sc, RED, True, [(200, 80), (250, 80), (300, 200)], 2)

pygame.draw.cicrle(sc, BLUE, (300, 250))













pygame.display.update()















clock = pygame.time.Clock()
FPS = 60
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False

    clock.tick(FPS)