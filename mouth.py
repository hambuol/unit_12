import pygame

class Mouth(pygame.sprite.Sprite):

    def __init__(self, screen):
        super().__init__()
        self.image = pygame.image.load("mouth.jpg")
        self.rect = self.image.get_rect()
        self.screen = screen
        self.speedx = 5
        self.speedy = 5

