# written by oliver hamburger
# program is a game of chomper
# last modified 12/5/16

# imports needed moduels
import pygame, sys
import apple
import mouth
from pygame.locals import *
import random


def main():
    # set screen width and height
    SCREEN_WIDTH = 1000
    SCREEN_HEIGHT = 900
    # needed to start pygame
    pygame.init()
    mainsurface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
    pygame.display.set_caption("Chomper")

    # sets color to white
    WHITE = (255,255,255)
    # defines apple group
    appleGroup = pygame.sprite.Group()
    for x in range(15):
        """loop blits blits apples in random locations"""
        xpos = random.randint(0, 950)
        ypos = random.randint(0, 850)
        myapple = apple.Apple(mainsurface)
        myapple.rect.topleft = (xpos, ypos)
        myapple.add(appleGroup)
        mainsurface.blit(myapple.image, myapple.rect)

    # defines the mouth group
    mouthGroup = pygame.sprite.Group()
    # difines the mouth
    mymouth = mouth.Mouth(mainsurface)
    # defines size of the mouth
    mymouth.rect.topleft = (50, 50)
    # adds mouth to a sprite group
    mymouth.add(mouthGroup)
    # blits mouth to the screen
    mainsurface.blit(mymouth.image, mymouth.rect)
    # dfines the font and the label for the game over screen
    myfont = pygame.font.SysFont("Britannic Bold", 200)
    nlabel = myfont.render("Game Over", 1, (0, 0, 0))

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        # sets the frames per second of the game/animation
        clock = pygame.time.Clock()
        clock.tick(50)
        # fills the screen with white
        mainsurface.fill(WHITE)

        pressed = pygame.key.get_pressed()
        # moves mouth if key is pressed
        if pressed[pygame.K_UP]:
            mymouth.up()
        # moves mouth if key is pressed
        if pressed[pygame.K_DOWN]:
            mymouth.down()
        # moves mouth if key is pressed
        if pressed[pygame.K_LEFT]:
            mymouth.left()
        # moves mouth if key is pressed
        if pressed[pygame.K_RIGHT]:
            mymouth.right()
        mainsurface.blit(mymouth.image, mymouth.rect)
        # blits the apples to the screen
        for myapple in appleGroup:
            mainsurface.blit(myapple.image, myapple.rect)

        mymouth.collide(appleGroup)
        # displays game over when all the aplles are gone
        if len(appleGroup) == 0:
           mainsurface.blit(nlabel, (100, 400))
        # updates display
        pygame.display.update()
main()
