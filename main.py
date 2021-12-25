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

    cube = Cube(525, 698, 25, 0, 15, 250, 15, 'cube-3.png')
    surface = Surface(0, 773, 'Surface-1.jpg', 10)
    field = Field([[0], [1], [1], [0, 0], [1], [1], [0, 0, 0], [1], [1], [1]], 1920, 698, 50, ['barrier-2.png', 'barrier-1.png'])

    clock = pygame.time.Clock()

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
        if cube.is_jump:
            cube.jump(698)

        # barrier.move(10)
        # barrier.render(screen)
        # barrier1.move(10)
        # barrier1.render(screen)
        # barrier2.move(10)
        # barrier2.render(screen)
        field.move(10)
        field.render(screen)
        surface.move(10)
        surface.render(screen)
        cube.render(screen)
        # if cube.is_collision(field):
        #      pygame.quit()
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()