import pygame

class Mouth(pygame.sprite.Sprite):

    def __init__(self, screen):
        super().__init__()
        self.image = pygame.image.load("mouth.jpg")
        self.rect = self.image.get_rect()
        self.screen = screen
        self.speedx = 5
        self.speedy = 5
        self.hit = pygame.mixer.Sound("chomp.wav")
    def up(self):
        self.rect.top -= self.speedy

        if self.rect.right > self.screen.get_width() or self.rect.left < 0:
            self.speedx = self.speedx
        if self.rect.top > self.screen.get_height() or self.rect.top < 0:
            self.speedy = self.speedy
        if self.rect.bottom > self.screen.get_height():
            self.speedy = self.speedy

    def down(self):
        self.rect.top += self.speedy

        if self.rect.right > self.screen.get_width() or self.rect.left < 0:
            self.speedx = self.speedx
        if self.rect.top > self.screen.get_height() or self.rect.top < 0:
            self.speedy = self.speedy
        if self.rect.bottom > self.screen.get_height():
            self.speedy = self.speedy

    def left(self):
        self.rect.left -= self.speedx

        if self.rect.right > self.screen.get_width() or self.rect.left < 0:
            self.speedx = self.speedx
        if self.rect.top > self.screen.get_height() or self.rect.top < 0:
            self.speedy = self.speedy
        if self.rect.bottom > self.screen.get_height():
            self.speedy = self.speedy

    def right(self):
        self.rect.left += self.speedx

        if self.rect.right > self.screen.get_width() or self.rect.left < 0:
            self.speedx = self.speedx
        if self.rect.top > self.screen.get_height() or self.rect.top < 0:
            self.speedy = self.speedy
        if self.rect.bottom > self.screen.get_height():
            self.speedy = self.speedy

    def collide(self, spriteGroup):
        pygame.sprite.spritecollide(self, spriteGroup, True)
        self.hit.play()


