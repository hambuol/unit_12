import pygame

class Apple(pygame.sprite.Sprite):

    def __init__(self, screen):
        super().__init__()
        self.image = pygame.image.load("apple.jpg")
        self.rect = self.image.get_rect()
        self.screen = screen
