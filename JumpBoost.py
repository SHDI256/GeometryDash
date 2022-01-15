import pygame


class JumpBoost(pygame.sprite.Sprite):
    def __init__(self, start_x, start_y, width, image, speed):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load(image), (width, width))
        self.rect = self.image.get_rect()
        self.rect.x = start_x
        self.rect.y = start_y
        self.width = width
        self.speed = speed

    def update(self):
        self.rect.x -= self.speed