import pygame

class Apple(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("apple.jpg")
        self.rect = self.image.get_rect()

        pygame.init()
