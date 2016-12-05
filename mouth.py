# imports pygame moduel
import pygame


class Mouth(pygame.sprite.Sprite):
    """class sets what is needed for mouth"""

    def __init__(self, screen):
        super().__init__()
        self.image = pygame.image.load("mouth.jpg")
        self.rect = self.image.get_rect()
        self.screen = screen
        self.speedx = 10
        self.speedy = 10
        self.hit = pygame.mixer.Sound("chomp.wav")

    def up(self):
        """
        moves mouth up
        :param: none
        :return:none
        """
        if self.rect.top > 0:
            self.rect.top -= self.speedy

    def down(self):
        """
        moves mouth down
        :param: none
        :return: none
        """
        if self.rect.bottom < self.screen.get_height():
            self.rect.bottom += self.speedy



    def left(self):
        """
        moves mouth left
        :param: none
        :return: none
        """
        if self.rect.left > 0:
            self.rect.left -= self.speedx


    def right(self):
        """
        moves mouth right
        :param: none
        :return: none
        """
        if self.rect.right < self.screen.get_width():
            self.rect.left += self.speedx


    def collide(self, spriteGroup):
        """
        collie function deletes what the mouth is collided with and plays the sound
        :param spriteGroup:
        :return: none
        """
        if pygame.sprite.spritecollide(self, spriteGroup, True):
            self.hit.play()
