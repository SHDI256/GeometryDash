import pygame


class Surface:
    def __init__(self, start_x, start_y, image, quantity):
        self.start_x = start_x
        self.start_y = start_y
        self.image = pygame.transform.scale(pygame.image.load(image), (1920, 307))
        self.quantity = quantity
        self.common_x = [i * 1920 for i in range(self.quantity)]

    def move(self, speed):
        for i in range(len(self.common_x)):
            self.common_x[i] -= speed

    def render(self, screen):
        for i in self.common_x:
            screen.blit(self.image, (i, self.start_y))
