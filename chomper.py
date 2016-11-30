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

    appleGroup = pygame.sprite.Group()
    for x in range(10):
        xpos = random.randint(0,450)
        ypos = random.randint(0,450)
        myapple = apple.Apple(mainsurface)
        myapple.rect.topleft = (xpos, ypos)
        myapple.add(appleGroup)
        mainsurface.blit(myapple.image, myapple.rect)


    mouthGroup = pygame.sprite.Group()
    mymouth = mouth.Mouth(mainsurface)
    mymouth.rect.topleft = (50, 50)
    mymouth.add(mouthGroup)
    mainsurface.blit(mymouth.image, mymouth.rect)
    hit = pygame.mixer.Sound("chomp.wav")

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







        pygame.display.update()
main()