import pygame
from Barrier import *


class Field:
    def __init__(self, field, start_x, start_y, width, images, speed):
        self.start_x = start_x
        self.start_y = start_y
        self.width = width
        self.images = [pygame.transform.scale(pygame.image.load(i), (width, width)) for i in images]
        self.default_field = field
        self.field = []
        self.speed = speed
        for i, c in enumerate(field):
            tmp = []
            for j, br in enumerate(c):
                if br in (0, 1):
                    tmp.append(Barrier(start_x + i * width, start_y - j * width, 50, images[br], br, self.speed))
                else:
                    tmp.append(-1)
            self.field.append(tmp)

    def get_now_y(self, x):
        if (x - self.field[0][-1].rect.x) // 50 < 0 or (x - self.field[0][-1].rect.x) // 50 > len(self.field) - 1:
            return 723
        else:
            return -(len(self.field[(x - self.field[0][-1].rect.x) // 50]) * 50) + 723