import pygame


class Barrier:
    def __init__(self, start_x, start_y, width, image, type):
        self.start_x = start_x
        self.start_y = start_y
        self.width = width
        self.image = pygame.transform.scale(pygame.image.load(image), (width, width))
        self.type = type

    def move(self, speed):
        self.start_x -= speed

    def render(self, screen):
        screen.blit(self.image, (self.start_x, self.start_y))

    def is_collision(self, cube):
        if cube.is_jump:
            x1, y1 = cube.origin_x + cube.radius * 2, cube.origin_y
        else:
            x1, y1 = cube.x + cube.radius * 2, cube.y
        x2, y2 = self.start_x, self.start_y

        if x2 <= x1 <= x2 + self.width and ():
            return True
        else:
            return False