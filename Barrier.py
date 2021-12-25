import pygame


class Barrier(pygame.sprite.Sprite):
    def __init__(self, start_x, start_y, image, type):
        self.start_x = start_x
        self.start_y = start_y
        self.image = pygame.transform.scale(pygame.image.load(image), (50, 50))
        self.type = type

    def move(self, speed):
        self.start_x -= speed

    def render(self, screen):
        screen.blit(self.image, (self.start_x, self.start_y))
