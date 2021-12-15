import pygame
from GD import *


if __name__ == '__main__':
    pygame.init()

    running = True

    GD = GeometryDash()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        GD.render()

pygame.quit()
