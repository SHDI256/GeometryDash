import sys

import pygame
from Cube import *
from Surface import *
from Field import *
from JBField import *
from JumperField import *
from Music import *


class Level:
    def __init__(self, cube, surface, field, background, screen, speed, jb_field, jumper_field, music):
        self.cube = cube
        self.player = pygame.sprite.Group()
        self.player.add(self.cube)
        self.surface = surface
        self.field = field
        self.background = background
        self.music = Music(music)
        self.screen = screen
        self.is_start = False
        self.speed = speed
        self.jb_field = jb_field
        self.jumper_field = jumper_field
        self.barriers = pygame.sprite.Group()
        self.jb_group = pygame.sprite.Group()
        self.jumper_group = pygame.sprite.Group()
        self.pause = False

        for i in self.field.field:
            for j in i:
                if j != -1:
                    self.barriers.add(j)

        for i in self.jb_field.field:
            for j in i:
                if j != -1:
                    self.jb_group.add(j)

        for i in self.jumper_field.field:
            for j in i:
                if j != -1:
                    self.jumper_group.add(j)

    def start(self):
        self.is_start = True

    def update(self):
        if self.is_start:
            self.cube.rect.x += 20
            hits = pygame.sprite.spritecollide(self.cube, self.jumper_group, False)
            self.cube.rect.x -= 20
            if len(hits) != 0:
                if hits[0].type == 0:
                    self.cube.speed = self.cube.speed_start * 1.5
                elif hits[0].type == 1:
                    self.cube.speed = self.cube.speed_start / 2
                self.cube.is_jump = True
                self.cube.jump_orientation = True
                self.cube.c = 0

            if pygame.key.get_pressed()[pygame.K_SPACE]:
                hits = pygame.sprite.spritecollide(self.cube, self.jb_group, False)
                if len(hits) != 0:
                    if hits[0].type == 0:
                        self.cube.speed = self.cube.speed_start
                    elif hits[0].type == 1:
                        self.cube.speed = self.cube.speed_start / 2
                    self.cube.jump_orientation = True
                    self.cube.c = 0
                self.cube.is_jump = True

            hits = pygame.sprite.spritecollide(self.cube, self.barriers, False)
            for hit in hits:
                if hit.type == 1:
                    self.is_start = False
                elif hit.type == 0:
                    if self.cube.rect.y >= hit.rect.y and \
                            self.cube.rect.y + self.cube.radius * 2 <= hit.rect.y + hit.rect.y + hit.width \
                            and self.cube.rect.x + self.cube.radius < hit.rect.x + hit.width:
                        self.is_start = False

            self.screen.blit(self.background, (0, 0))
            self.surface.move(self.speed)
            self.surface.render(self.screen)
            self.barriers.update()
            self.barriers.draw(self.screen)
            self.jb_group.update()
            self.jb_group.draw(self.screen)
            self.jumper_group.update()
            self.jumper_group.draw(self.screen)
            self.player.update()
            self.player.draw(self.screen)


if __name__ == '__main__':
    pygame.mixer.pre_init(44100, -16, 1, 512)
    pygame.init()

    screen = pygame.display.set_mode((1920, 1080))

    background = pygame.image.load('background-1.jpg')
    background = pygame.transform.scale(background, (1920, 1080))
    screen.blit(background, (0, 0))

    clock = pygame.time.Clock()

    surface = Surface(0, 773, 'Surface-1.jpg', 10)

    field = Field(
        [[0]] * 1000 + [[-1, 0], [-1, 0], [0], [1], [1], [1], [1], [1], [1], [1], [-1, 0], [-1, 0], [-1, 0], [-1, 0],
         [1], [1], [0, 0], [0, 0], [1], [1], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 1],
         [0, 0, 1], [0, 0], [0, 0],
         [0, 0], [0, 0], [0, 0], [0, 0], [1], [1], [1], [0, 0], [0, 0],
         [], [], [], [], [], [], [], [], [], [], [0, 0], [0, 0], [0, 0], [1], [1], [0, 0, 0, 0], [0, 0, 0, 0],
         [1], [1], [1], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [1], [1], [1], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0],
         [1], [1], [1], [0], [0], [0], [1], [1],
         [0, 0], [0, 0], [1], [1], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0],
         [0], [0],
         [0], [0], [0], [0], [0], [0], [0], [0], [1], [1], [1], [1], [1], [1], [1], [], [], [], [], []]
        , 1920, 723, 50,
        ['barrier-2.png', 'barrier-1.png'], 11)

    jbfield = JBField(
        [[]] * 1000 + [[], [], [], [], [], [], [-1, -1, -1, -1, 0], [], [], [], [], [], [],
         [],
         [], [], [], [], [], [], [], [], [], [], [], [],
         [], [], [],
         [], [], [], [], [], [], [], [], [],
         [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [],
         [], [], [], [], [], [], [], [], [], [],
         [], [], [], [], [], [], [], [],
         [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [],
         [], [], [], [], [], [], [], [], [], [], [], [-1, -1, 1], [], [], [], [], [], []]
        , 1920, 723, 50, ['jump_boost-1.png', 'jump_boost-2.png'], 11)

    jumperField = JumperField(
        [[]] * 1000 + [[], [], [], [], [], [], [], [], [], [], [], [], [],
         [],
         [], [], [], [], [], [], [], [], [], [], [], [],
         [], [], [],
         [], [], [], [], [], [], [], [], [],
         [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [],
         [], [], [], [], [], [], [], [], [], [],
         [], [], [], [], [], [], [], [],
         [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [],
         [], [], [], [-1, 0], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
        , 1920, 723, 50, ['jumper-1.png', 'jumper-2.png'], 11)
    cube = Cube(525, 723, 25, 50, 10, 'cube-3.png', field)

    level = Level(cube, surface, field, background, screen, 11, jbfield, jumperField, 'gd1.mp3')

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        if not level.is_start:
            level.start()

        level.update()

        if not level.is_start:
            surface = Surface(0, 773, 'Surface-1.jpg', 10)
            field = Field(
                [[-1, 0], [-1, 0], [0], [1], [1], [1], [1], [1], [1], [1], [-1, 0], [-1, 0], [-1, 0], [-1, 0],
                 [1], [1], [0, 0], [0, 0], [1], [1], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 1],
                 [0, 0, 1], [0, 0], [0, 0],
                 [0, 0], [0, 0], [0, 0], [0, 0], [1], [1], [1], [0, 0], [0, 0],
                 [], [], [], [], [], [], [], [], [], [], [0, 0], [0, 0], [0, 0], [1], [1], [0, 0, 0, 0], [0, 0, 0, 0],
                 [1], [1], [1], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [1], [1], [1], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0],
                 [1], [1], [1], [0], [0], [0], [1], [1],
                 [0, 0], [0, 0], [1], [1], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0],
                 [0], [0],
                 [0], [0], [0], [0], [0], [0], [0], [0], [1], [1], [1], [1], [1], [1], [1], [], [], [], [], []]
                , 1920, 723, 50,
                ['barrier-2.png', 'barrier-1.png'], 11)

            jbfield = JBField(
                [[], [], [], [], [], [], [-1, -1, -1, -1, 0], [], [], [], [], [], [],
                 [],
                 [], [], [], [], [], [], [], [], [], [], [], [],
                 [], [], [],
                 [], [], [], [], [], [], [], [], [],
                 [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [],
                 [], [], [], [], [], [], [], [], [], [],
                 [], [], [], [], [], [], [], [],
                 [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [],
                 [], [], [], [], [], [], [], [], [], [], [], [-1, -1, 1], [], [], [], [], [], []]
                , 1920, 723, 50, ['jump_boost-1.png', 'jump_boost-2.png'], 11)

            jumperField = JumperField(
                [[], [], [], [], [], [], [], [], [], [], [], [], [],
                 [],
                 [], [], [], [], [], [], [], [], [], [], [], [],
                 [], [], [],
                 [], [], [], [], [], [], [], [], [],
                 [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [],
                 [], [], [], [], [], [], [], [], [], [],
                 [], [], [], [], [], [], [], [],
                 [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [],
                 [], [], [], [-1, 0], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
                , 1920, 723, 50, ['jumper-1.png', 'jumper-2.png'], 11)
            cube = Cube(525, 723, 25, 50, 10, 'cube-3.png', field)
            level = Level(cube, surface, field, background, screen, 11, jbfield, jumperField, 'gd1.mp3')
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()