import main
import pygame
import mm
import myHelp

pygame.init()


pygame.display.set_caption('Crystal Collector')
open_m = True
running = True
a = 0
while running:
    if open_m == True:
        a = mm.menu()
    if a == 'game':
        open_m = False
        main.main()
        open_m = True


    if a == 'exit':
        running = False

    if a == 'help':
        open_m = False
        myHelp.helpGAME()
        open_m = True


pygame.quit()

