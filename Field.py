import pygame
from Barrier import *


class Field:
    def __init__(self, field, start_x, start_y, width, images):
        self.start_x = start_x
        self.start_y = start_y
        self.width = width
        self.images = [pygame.transform.scale(pygame.image.load(i), (width, width)) for i in images]
        self.field = []
        for i, c in enumerate(field):
            tmp = []
            for j, br in enumerate(c):
                if br != -1:
                    tmp.append(Barrier(start_x + i * width, start_y - j * width, 50, images[br], br))
            self.field.append(tmp)
        print(self.field)


    def move(self, speed):
        for barriers in self.field:
            for barrier in barriers:
                if barrier != -1:
                    barrier.start_x -= speed

    def render(self, screen):
        for i, barriers in enumerate(self.field):
            for j, barrier in enumerate(barriers):
                if barrier != -1:
                    barrier.render(screen)


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
