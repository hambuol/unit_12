import pygame,sys
import apple
import mouth
from pygame.locals import *
import random
def main():
    SCREEN_WIDTH = 500
    SCREEN_HEIGHT = 500
    pygame.init()
    mainsurface = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT), 0, 32)
    pygame.display.set_caption("chomper")
    WHITE = (255,255,255)
    RED = (255,0,0)
    mainsurface.fill(WHITE)
    appleGroup = pygame.sprite.Group()
    mouthGroup = pygame.sprite.Group()
    mymouth = mouth.Mouth(mainsurface)
    mymouth.rect.topleft = (50, 50)
    mymouth.add(mouthGroup)
    mainsurface.blit(mymouth.image, mymouth.rect)
    def appl():
        for x in range(10):
            xpos = random.randint(100,450)
            ypos = random.randint(100,450)
            myapple = apple.Apple()
            myapple.rect.topleft = (xpos, ypos)
            myapple.add(appleGroup)
            mainsurface.blit(myapple.image, myapple.rect)

    appl()
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        clock = pygame.time.Clock()
        clock.tick(10)
        #appl()
        mainsurface.blit(mymouth.image, mymouth.rect)
        pygame.display.update()
main()