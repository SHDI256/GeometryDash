import pygame
from JumpBoost import *


class JBField:
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
                    tmp.append(JumpBoost(start_x + i * width, start_y - j * width, 50, images[br], self.speed, br))
                else:
                    tmp.append(-1)
            self.field.append(tmp)