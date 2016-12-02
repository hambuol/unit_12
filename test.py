import pygame,sys
from pygame.locals import *

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 900
pygame.init()
mainsurface = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT), 0, 32)

pygame.draw.rect(mainsurface, (255, 0, 0), (130, 50, 50, 130), 0)
pygame.draw.circle(mainsurface, (0,0,255), (375, 250), 100)





while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()



