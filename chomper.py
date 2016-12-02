import pygame,sys
import apple
import mouth
from pygame.locals import *
import random
def main():
    SCREEN_WIDTH = 1000
    SCREEN_HEIGHT = 900
    pygame.init()
    mainsurface = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT), 0, 32)
    pygame.display.set_caption("Chomper")
    WHITE = (255,255,255)

    appleGroup = pygame.sprite.Group()
    for x in range(15):
        xpos = random.randint(0,950)
        ypos = random.randint(0,850)
        myapple = apple.Apple(mainsurface)
        myapple.rect.topleft = (xpos, ypos)
        myapple.add(appleGroup)
        mainsurface.blit(myapple.image, myapple.rect)


    mouthGroup = pygame.sprite.Group()
    mymouth = mouth.Mouth(mainsurface)
    mymouth.rect.topleft = (50, 50)
    mymouth.add(mouthGroup)
    mainsurface.blit(mymouth.image, mymouth.rect)
    myfont = pygame.font.SysFont("Britannic Bold", 200)
    nlabel = myfont.render("Game Over", 1, (0, 0, 0))


    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        clock = pygame.time.Clock()
        clock.tick(50)
        mainsurface.fill(WHITE)
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]:
            mymouth.up()
        if pressed[pygame.K_DOWN]:
            mymouth.down()
        if pressed[pygame.K_LEFT]:
            mymouth.left()
        if pressed[pygame.K_RIGHT]:
            mymouth.right()
        mainsurface.blit(mymouth.image, mymouth.rect)
        for myapple in appleGroup:
            mainsurface.blit(myapple.image, myapple.rect)

        mymouth.collide(appleGroup)

        if len(appleGroup) == 0:
            mainsurface.blit(nlabel, (100, 400))







        pygame.display.update()
main()