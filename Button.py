import pygame


class Button(pygame.sprite.Sprite):
    def __init__(self, x, y, image, width, height, func):
        pygame.sprite.Sprite.__init__(self)
        self.width = width
        self.height = height
        self.func = func
        self.image = pygame.transform.scale(pygame.image.load(image), (self.width, self.height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def clicked(self):
        self.func()