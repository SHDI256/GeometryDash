import pygame


class GeometryDash:
    def __init__(self, cube, surface, map, speed):
        self.cube = cube
        self.surface = surface
        self.map = map
        self.speed = speed

    def generation(self):
        if self.cube.is_jump:
            self.cube.jump()

