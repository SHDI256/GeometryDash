import sys

import pygame
from Cube import *
from Surface import *
from Field import *
from JumpBoost import *

class Level:
    def __init__(self, cube, surface, field, background, screen, speed, jb, music=None):
        self.cube = cube
        self.player = pygame.sprite.Group()
        self.player.add(self.cube)
        self.surface = surface
        self.field = field
        self.background = background
        self.music = music
        self.screen = screen
        self.is_start = False
        self.speed = speed
        self.barriers = pygame.sprite.Group()
        self.jb_group = pygame.sprite.Group()
        [[self.barriers.add(j) for j in i] for i in self.field.field]
        [self.jb_group.add(i) for i in jb]

    def start(self):
        self.is_start = True

    def draw(self):
        self.screen.blit(self.background, (0, 0))
        self.surface.render(self.screen)
        self.barriers.update()
        self.barriers.draw(self.screen)
        self.jb_group.update()
        self.jb_group.draw(self.screen)
        self.player.update()
        self.player.draw(self.screen)

    def update(self):
        if self.is_start:
            if pygame.key.get_pressed()[pygame.K_SPACE]:
                hits = pygame.sprite.spritecollide(self.cube, self.jb_group, False)
                if len(hits) != 0:
                    self.cube.speed = self.cube.speed_start
                    self.cube.is_jump = True
                    self.cube.jump_orientation = True
                    self.cube.c = 0
                self.cube.is_jump = True

            self.screen.blit(self.background, (0, 0))
            hits = pygame.sprite.spritecollide(self.cube, self.barriers, False)
            for hit in hits:
                if hit.type == 1:
                    self.is_start = False
                else:
                    if self.cube.rect.y >= hit.rect.y and self.cube.rect.y + self.cube.radius * 2 <= hit.rect.y + hit.rect.y + hit.width and self.cube.rect.x + self.cube.radius < hit.rect.x + hit.width:
                        self.is_start = False

            self.surface.move(self.speed)
            self.surface.render(self.screen)
            self.barriers.update()
            self.barriers.draw(self.screen)
            self.jb_group.update()
            self.jb_group.draw(self.screen)
            self.player.update()
            self.player.draw(self.screen)


if __name__ == '__main__':
    pygame.init()

    screen = pygame.display.set_mode((1920, 1080))

    background = pygame.image.load('background-1.jpg')
    background = pygame.transform.scale(background, (1920, 1080))
    screen.blit(background, (0, 0))

    surface = Surface(0, 773, 'Surface-1.jpg', 10)
    field = Field([[0], [0], [0], [0], [0], [1], [1], [0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0, 1],
                   [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0], [0],
                   [0, 0, 0, 0], [0, 0, 0, 0], [0], [0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0], [0],
                   [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [1], [1], [1], [1], [1], [1], [1]],
                  1920, 723, 50, ['barrier-2.png', 'barrier-1.png'], 11)
    cube = Cube(525, 723, 25, 50, 10, 'cube-3.png', field)

    jump_boost1 = JumpBoost(1000, 600, 50, 'jump_boost-1.png', 11)

    clock = pygame.time.Clock()

    barriers = pygame.sprite.Group()
    [[barriers.add(j) for j in i] for i in field.field]

    running = True

    level = Level(cube, surface, field, background, screen, 11, [jump_boost1])

    level.draw()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        if not level.is_start:
            level.start()

        level.update()

        if not level.is_start:
            jump_boost1 = JumpBoost(1000, 600, 50, 'jump_boost-1.png', 11)
            surface = Surface(0, 773, 'Surface-1.jpg', 10)
            field = Field(
                [[0], [0], [0], [0], [0], [1], [1], [0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0, 1], [0, 0], [0, 0],
                 [0, 0], [0, 0], [0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0], [0], [0, 0, 0, 0], [0, 0, 0, 0], [0],
                 [0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0], [0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]], 1920, 723,
                50, ['barrier-2.png', 'barrier-1.png'], 11)
            cube = Cube(525, 723, 25, 50, 10, 'cube-3.png', field)
            level = Level(cube, surface, field, background, screen, 11, [jump_boost1])

        pygame.display.flip()
        clock.tick(60)
    pygame.quit()