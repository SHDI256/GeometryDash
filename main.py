import sys

import pygame
from Cube import *
from Surface import *
from Barrier import *
from Field import *

if __name__ == '__main__':
    pygame.init()

    screen = pygame.display.set_mode((1920, 1080))

    background = pygame.image.load('background-1.jpg')
    background = pygame.transform.scale(background, (1920, 1080))
    screen.blit(background, (0, 0))

    surface = Surface(0, 773, 'Surface-1.jpg', 10)
    field = Field([[0], [0], [0], [0], [0], [0], [0], [0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]], 1920, 723, 50, ['barrier-2.png', 'barrier-1.png'], 10)
    cube = Cube(525, 723, 25, 50, 12, 'cube-3.png', field)
    clock = pygame.time.Clock()

    player = pygame.sprite.Group()
    player.add(cube)

    barriers = pygame.sprite.Group()
    [[barriers.add(j) for j in i] for i in field.field]

    running = True
    is_jump = False

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if not cube.is_jump:
                        cube.is_jump = True

        screen.blit(background, (0, 0))
        hits = pygame.sprite.spritecollide(cube, barriers, False)
        for hit in hits:
            if hit.type == 1:
                running = False
            else:
                if cube.rect.y + cube.radius * 2 > hit.rect.y:
                    running = False
        surface.move(10)
        surface.render(screen)
        barriers.update()
        barriers.draw(screen)
        player.update()
        player.draw(screen)
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()