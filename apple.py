# imports needed moduels
import pygame


class Apple(pygame.sprite.Sprite):
    """class sets what is needed for the apples"""

    def __init__(self, screen):
        super().__init__()
        self.image = pygame.image.load("apple.jpg")
        self.rect = self.image.get_rect()
        self.screen = screen
