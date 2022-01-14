import pygame
from Barrier import *


class Field:
    def __init__(self, field, start_x, start_y, width, images, speed):
        self.start_x = start_x
        self.start_y = start_y
        self.width = width
        self.images = [pygame.transform.scale(pygame.image.load(i), (width, width)) for i in images]
        self.field = []
        self.speed = speed
        for i, c in enumerate(field):
            tmp = []
            for j, br in enumerate(c):
                if br != -1:
                    tmp.append(Barrier(start_x + i * width, start_y - j * width, 50, images[br], br, self.speed))
            self.field.append(tmp)

    def get_now_y(self, x):
        if (x - self.field[0][0].rect.x) // 50 < 0 or (x - self.field[0][0].rect.x) // 50 > len(self.field) - 1:
            return 723
        else:
            return -(len(self.field[(x - self.field[0][0].rect.x) // 50]) * 50) + 723


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
