import pygame
from Barrier import *


class Field:
    def __init__(self, field, start_x, start_y, width, images):
        self.field = field
        self.start_x = start_x
        self.start_y = start_y
        self.width = width
        self.images = [pygame.transform.scale(pygame.image.load(i), (width, width)) for i in images]

    def move(self, speed):
        self.start_x -= speed

    def render(self, screen):
        for i, barriers in enumerate(self.field):
            for j, barrier in enumerate(barriers):
                if barrier != -1:
                    screen.blit(self.images[barrier], (self.start_x + self.width * i, self.start_y - self.width * j))


if __name__ == '__main__':
    pygame.init()

    screen = pygame.display.set_mode((1920, 1080))

    background = pygame.image.load('background-1.jpg')
    background = pygame.transform.scale(background, (1920, 1080))
    screen.blit(background, (0, 0))

    field = Field([[0, 0, 0], [-1, 0, 0], [-1, 0, 1]], 1920, 723, 50, ['barrier-2.png', 'barrier-1.png'])

    clock = pygame.time.Clock()

    running = True
    is_jump = False

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.blit(background, (0, 0))

        field.move(10)
        field.render(screen)

        pygame.display.flip()
        clock.tick(60)
    pygame.quit()
