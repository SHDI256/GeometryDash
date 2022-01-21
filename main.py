import sys

import pygame
from Cube import *
from Surface import *
from Field import *
from JBField import *
from JumperField import *
from Level import *
from MainScreen import *
from Button import *
from ChooseLevel import *
from Pause import *
import random

GAME_STATUS = 'MAIN_SCREEN'
LEVEL = -1
CUBE_IMAGE = 'cube-3.png'

def update_fields():
    global surface1, surface2, surface3, field1, field2, field3, jbfield1, jbfield2, jbfield3, jumperField1, jumperField2, jumperField3, cube1, cube2, cube3

    surface1 = Surface(0, 773, 'Surface-1.jpg', 10)
    surface2 = Surface(0, 773, 'Surface-1.jpg', 10)
    surface3 = Surface(0, 773, 'Surface-1.jpg', 10)

    field1 = Field(
        [[-1, 0], [-1, 0], [-1, 0], [1], [1], [1], [1], [1], [1], [1], [-1, 0], [-1, 0], [-1, 0], [-1, 0],
         [1], [1], [0, 0], [0, 0], [1], [1], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0],
         [0, 0, 1],
         [0, 0, 1], [0, 0], [0, 0],
         [0, 0], [0, 0], [0, 0], [0, 0], [1], [1], [1], [0, 0], [0, 0],
         [], [], [], [], [], [], [], [], [], [], [0, 0], [0, 0], [0, 0], [1], [1], [0, 0, 0, 0],
         [0, 0, 0, 0],
         [1], [1], [1], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [1], [1], [1], [0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0],
         [1], [1], [1], [0], [0], [0], [1], [1],
         [0, 0], [0, 0], [1], [1], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0],
         [0], [0], [0], [0], [0], [], [], [], [], [], [-1, -1, -1, -1, 0, 1], [], [], [], [], [],
         [], [0], [0], [0], [0], [0], [1], [1], [1], [1], [1], [1], [0, 1],
         [0, 1], [0, 1], [0, 1], [-1, 0, 1], [-1, 0, 1], [-1, 0, 1],
         [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [1],
         [1, -1, -1, 0], [1],
         [1, -1, -1, 0], [1], [1, -1, -1, 0], [1], [], [], [], [], [], [], [], [0, 0], [0, 0], [0, 0], [1],
         [1],
         [0, 0, 0, 0],
         [0, 0, 0, 0],
         [1], [1], [1], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [1], [1], [1], [0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0],
         [1], [1], [1], [0], [0], [0], [1], [1],
         [0, 0], [0, 0], [1], [1], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0],
         [-1, 0], [-1, 0], [-1, 0], [1], [1], [1], [1], [1], [1], [1], [-1, 0], [-1, 0], [-1, 0], [-1, 0],
         [1], [1], [0, 0], [0, 0], [1], [1], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0],
         [0, 0, 1],
         [0, 0, 1], [0, 0], [0, 0],
         [0, 0], [0, 0], [0, 0], [0, 0], [1], [1], [1], [0, 0], [0, 0],
         ]

        , 1920, 723, 50,
        ['barrier-2.png', 'barrier-1.png'], 11)

    jbfield1 = JBField(
        [[], [], [], [], [], [], [], [-1, -1, -1, -1, 0], [], [], [], [], [], [],
         [],
         [], [], [], [], [], [], [], [], [], [], [], [],
         [], [], [],
         [], [], [], [], [], [], [], [], [],
         [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [],
         [], [], [], [], [], [], [], [], [], [],
         [], [], [], [], [], [], [], [],
         [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [],
         [], [], [], [], [], [], [], [], [], [], [], [], [], [], [],
         [], [], [], [], [-1, -1, 0], [], [], [], [], [], [-1, -1, -1, 0], [], [], [], [],
         [-1, -1, -1, -1, 0], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [],
         [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [],
         [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [],
         [-1, -1, -1, -1, 0], [], [], [], [], [], [], [], [], [], [], [], [], []]
        , 1920, 723, 50, ['jump_boost-1.png', 'jump_boost-2.png'], 11)

    jumperField1 = JumperField(
        [[], [], [-1, -1, 0], [], [], [], [], [], [], [], [], [], [], [],
         [],
         [], [], [], [], [], [], [], [], [], [], [], [],
         [], [], [],
         [], [], [], [], [], [], [], [], [],
         [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [],
         [], [], [], [], [], [], [], [], [], [],
         [], [], [], [], [], [], [], [],
         [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [],
         [], [0], [], [], [], [], [], [], [], [], [], [], [], [],
         [], [], [], [], [], [], [], [], [], [], [], [], [], [], [],
         [], [], [], [], [], [], [], [-1, -1, -1, -1, 1], [], [-1, -1, -1, -1, 1], [], [-1, -1, -1, -1, 1],
         [], [-1, -1, -1, -1, 1]]
        , 1920, 723, 50, ['jumper-1.png', 'jumper-2.png'], 11)

    field2 = Field(
        [[-1, 0], [-1, 0], [-1, 0], [1], [1], [1], [1], [1], [1], [1], [-1, 0], [-1, 0], [-1, 0], [-1, 0],
         [1], [1], [0, 0], [0, 0], [1], [1], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0],
         [0, 0, 1],
         [0, 0, 1], [0, 0], [0, 0],
         [0, 0], [0, 0], [0, 0], [0, 0], [1], [1], [1], [0, 0], [0, 0],
         [], [], [], [], [], [], [], [], [], [], [0, 0], [0, 0], [0, 0], [1], [1], [0, 0, 0, 0],
         [0, 0, 0, 0],
         [1], [1], [1], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [1], [1], [1], [0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0],
         [1], [1], [1], [0], [0], [0], [1], [1],
         [0, 0], [0, 0], [1], [1], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0],
         [0], [0], [0], [0], [0], [], [], [], [], [], [-1, -1, -1, -1, 0, 1], [], [], [], [], [],
         [], [0], [0], [0], [0], [0], [1], [1], [1], [1], [1], [1], [0, 1],
         [0, 1], [0, 1], [0, 1], [-1, 0, 1], [-1, 0, 1], [-1, 0, 1],
         [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [1],
         [1, -1, -1, 0], [1],
         [1, -1, -1, 0], [1], [1, -1, -1, 0], [1], [], [], [], [], [], [], [], [0, 0], [0, 0], [0, 0], [1],
         [1],
         [0, 0, 0, 0],
         [0, 0, 0, 0],
         [1], [1], [1], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [1], [1], [1], [0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0],
         [1], [1], [1], [0], [0], [0], [1], [1],
         [0, 0], [0, 0], [1], [1], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0],
         [-1, 0], [-1, 0], [-1, 0], [1], [1], [1], [1], [1], [1], [1], [-1, 0], [-1, 0], [-1, 0], [-1, 0],
         [1], [1], [0, 0], [0, 0], [1], [1], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0],
         [0, 0, 1],
         [0, 0, 1], [0, 0], [0, 0],
         [0, 0], [0, 0], [0, 0], [0, 0], [1], [1], [1], [0, 0], [0, 0],
         ]

        , 1920, 723, 50,
        ['barrier-2.png', 'barrier-1.png'], 11)

    jbfield2 = JBField(
        [[], [], [], [], [], [], [], [-1, -1, -1, -1, 0], [], [], [], [], [], [],
         [],
         [], [], [], [], [], [], [], [], [], [], [], [],
         [], [], [],
         [], [], [], [], [], [], [], [], [],
         [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [],
         [], [], [], [], [], [], [], [], [], [],
         [], [], [], [], [], [], [], [],
         [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [],
         [], [], [], [], [], [], [], [], [], [], [], [], [], [], [],
         [], [], [], [], [-1, -1, 0], [], [], [], [], [], [-1, -1, -1, 0], [], [], [], [],
         [-1, -1, -1, -1, 0], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [],
         [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [],
         [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [],
         [-1, -1, -1, -1, 0], [], [], [], [], [], [], [], [], [], [], [], [], []]
        , 1920, 723, 50, ['jump_boost-1.png', 'jump_boost-2.png'], 11)

    jumperField2 = JumperField(
        [[], [], [-1, -1, 0], [], [], [], [], [], [], [], [], [], [], [],
         [],
         [], [], [], [], [], [], [], [], [], [], [], [],
         [], [], [],
         [], [], [], [], [], [], [], [], [],
         [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [],
         [], [], [], [], [], [], [], [], [], [],
         [], [], [], [], [], [], [], [],
         [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [],
         [], [0], [], [], [], [], [], [], [], [], [], [], [], [],
         [], [], [], [], [], [], [], [], [], [], [], [], [], [], [],
         [], [], [], [], [], [], [], [-1, -1, -1, -1, 1], [], [-1, -1, -1, -1, 1], [], [-1, -1, -1, -1, 1],
         [], [-1, -1, -1, -1, 1]]
        , 1920, 723, 50, ['jumper-1.png', 'jumper-2.png'], 11)

    field3 = Field(
        [[-1, 0], [-1, 0], [-1, 0], [1], [1], [1], [1], [1], [1], [1], [-1, 0], [-1, 0], [-1, 0], [-1, 0],
         [1], [1], [0, 0], [0, 0], [1], [1], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0],
         [0, 0, 1],
         [0, 0, 1], [0, 0], [0, 0],
         [0, 0], [0, 0], [0, 0], [0, 0], [1], [1], [1], [0, 0], [0, 0],
         [], [], [], [], [], [], [], [], [], [], [0, 0], [0, 0], [0, 0], [1], [1], [0, 0, 0, 0],
         [0, 0, 0, 0],
         [1], [1], [1], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [1], [1], [1], [0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0],
         [1], [1], [1], [0], [0], [0], [1], [1],
         [0, 0], [0, 0], [1], [1], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0],
         [0], [0], [0], [0], [0], [], [], [], [], [], [-1, -1, -1, -1, 0, 1], [], [], [], [], [],
         [], [0], [0], [0], [0], [0], [1], [1], [1], [1], [1], [1], [0, 1],
         [0, 1], [0, 1], [0, 1], [-1, 0, 1], [-1, 0, 1], [-1, 0, 1],
         [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [1],
         [1, -1, -1, 0], [1],
         [1, -1, -1, 0], [1], [1, -1, -1, 0], [1], [], [], [], [], [], [], [], [0, 0], [0, 0], [0, 0], [1],
         [1],
         [0, 0, 0, 0],
         [0, 0, 0, 0],
         [1], [1], [1], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [1], [1], [1], [0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0],
         [1], [1], [1], [0], [0], [0], [1], [1],
         [0, 0], [0, 0], [1], [1], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0],
         [-1, 0], [-1, 0], [-1, 0], [1], [1], [1], [1], [1], [1], [1], [-1, 0], [-1, 0], [-1, 0], [-1, 0],
         [1], [1], [0, 0], [0, 0], [1], [1], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0],
         [0, 0, 1],
         [0, 0, 1], [0, 0], [0, 0],
         [0, 0], [0, 0], [0, 0], [0, 0], [1], [1], [1], [0, 0], [0, 0],
         ]

        , 1920, 723, 50,
        ['barrier-2.png', 'barrier-1.png'], 11)

    jbfield3 = JBField(
        [[], [], [], [], [], [], [], [-1, -1, -1, -1, 0], [], [], [], [], [], [],
         [],
         [], [], [], [], [], [], [], [], [], [], [], [],
         [], [], [],
         [], [], [], [], [], [], [], [], [],
         [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [],
         [], [], [], [], [], [], [], [], [], [],
         [], [], [], [], [], [], [], [],
         [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [],
         [], [], [], [], [], [], [], [], [], [], [], [], [], [], [],
         [], [], [], [], [-1, -1, 0], [], [], [], [], [], [-1, -1, -1, 0], [], [], [], [],
         [-1, -1, -1, -1, 0], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [],
         [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [],
         [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [],
         [-1, -1, -1, -1, 0], [], [], [], [], [], [], [], [], [], [], [], [], []]
        , 1920, 723, 50, ['jump_boost-1.png', 'jump_boost-2.png'], 11)

    jumperField3 = JumperField(
        [[], [], [-1, -1, 0], [], [], [], [], [], [], [], [], [], [], [],
         [],
         [], [], [], [], [], [], [], [], [], [], [], [],
         [], [], [],
         [], [], [], [], [], [], [], [], [],
         [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [],
         [], [], [], [], [], [], [], [], [], [],
         [], [], [], [], [], [], [], [],
         [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [],
         [], [0], [], [], [], [], [], [], [], [], [], [], [], [],
         [], [], [], [], [], [], [], [], [], [], [], [], [], [], [],
         [], [], [], [], [], [], [], [-1, -1, -1, -1, 1], [], [-1, -1, -1, -1, 1], [], [-1, -1, -1, -1, 1],
         [], [-1, -1, -1, -1, 1]]
        , 1920, 723, 50, ['jumper-1.png', 'jumper-2.png'], 11)

    cube1 = Cube(525, 723, 25, 50, 10, CUBE_IMAGE, field1)
    cube2 = Cube(525, 723, 25, 50, 10, CUBE_IMAGE, field2)
    cube3 = Cube(525, 723, 25, 50, 10, CUBE_IMAGE, field3)

if __name__ == '__main__':
    pygame.mixer.pre_init(44100, -16, 1, 512)
    pygame.init()

    screen = pygame.display.set_mode((1920, 1080))

    background = pygame.image.load('background-1.jpg')
    background = pygame.transform.scale(background, (1920, 1080))

    clock = pygame.time.Clock()

    update_fields()

    pause_start_btn = Button(700, 600, 'Button-start.png', 150, 150, lambda: LEVEL[0].start)

    cube_btn_1 = Button(1000, 100, 'cube-1.png', 200, 200, lambda: None)
    cube_btn_2 = Button(1000, 400, 'cube-2.png', 200, 200, lambda: None)
    cube_btn_3 = Button(1000, 700, 'cube-3.png', 200, 200, lambda: None)

    pause_screen = PauseScreen('ch_lvl_back.jpg', pause_start_btn, cube_btn_1, cube_btn_2, cube_btn_3, screen)

    choose_btn_1 = Button(100, 100, 'Level-1.png', 813, 158, pygame.quit)
    choose_btn_2 = Button(100, 400, 'Level-2.png', 813, 158, pygame.quit)
    choose_btn_3 = Button(100, 700, 'Level-3.png', 813, 158, pygame.quit)

    choose_lvl_screen = ChooseLevelScreen('ch_lvl_back.jpg', choose_btn_1, choose_btn_2, choose_btn_3, screen)

    start_btn = Button(885, 600, 'Button-start.png', 150, 150, choose_lvl_screen.render)
    main_screen = MainScreen('Main-screen.jpg', start_btn, screen)

    main_screen.render()

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and GAME_STATUS == 'MAIN_SCREEN':
                if start_btn.rect.x <= event.pos[0] <= start_btn.rect.x + start_btn.width and \
                        start_btn.rect.y < event.pos[1] < start_btn.rect.y + start_btn.height:
                    GAME_STATUS = 'CHOOSE_LEVEL'
                    start_btn.clicked()
            elif event.type == pygame.MOUSEBUTTONDOWN and GAME_STATUS == 'CHOOSE_LEVEL':
                if choose_btn_1.rect.x <= event.pos[0] <= choose_btn_1.rect.x + choose_btn_1.width and \
                        choose_btn_1.rect.y < event.pos[1] < choose_btn_1.rect.y + choose_btn_1.height:
                    GAME_STATUS = 'LEVEL'
                    level1 = Level(cube1, surface1, field1, background, screen, 11, jbfield1, jumperField1, 'gd1.mp3')
                    LEVEL = [level1, 1]
                    LEVEL[0].music.start()
                elif choose_btn_2.rect.x <= event.pos[0] <= choose_btn_2.rect.x + choose_btn_2.width and \
                        choose_btn_2.rect.y < event.pos[1] < choose_btn_2.rect.y + choose_btn_2.height:
                    GAME_STATUS = 'LEVEL'
                    level2 = Level(cube2, surface2, field2, background, screen, 11, jbfield2, jumperField2, 'gd1.mp3')
                    LEVEL = [level2, 2]
                    LEVEL[0].music.start()
                elif choose_btn_3.rect.x <= event.pos[0] <= choose_btn_3.rect.x + choose_btn_3.width and \
                        choose_btn_3.rect.y < event.pos[1] < choose_btn_3.rect.y + choose_btn_3.height:
                    GAME_STATUS = 'LEVEL'
                    level3 = Level(cube3, surface3, field3, background, screen, 11, jbfield3, jumperField3, 'gd3.mp3')
                    LEVEL = [level3, 3]
                    LEVEL[0].music.start()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE and GAME_STATUS == 'LEVEL':
                LEVEL[0].music.stop()
                GAME_STATUS = 'PAUSE'
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE and GAME_STATUS == 'PAUSE':
                update_fields()
                GAME_STATUS = 'CHOOSE_LEVEL'
            elif event.type == pygame.MOUSEBUTTONDOWN and GAME_STATUS == 'PAUSE':
                if pause_start_btn.rect.x <= event.pos[0] <= pause_start_btn.rect.x + pause_start_btn.width and \
                        pause_start_btn.rect.y < event.pos[1] < pause_start_btn.rect.y + pause_start_btn.height:
                    GAME_STATUS = 'LEVEL'
                    LEVEL[0].music.start()
                elif cube_btn_1.rect.x <= event.pos[0] <= cube_btn_1.rect.x + cube_btn_1.width and \
                        cube_btn_1.rect.y < event.pos[1] < cube_btn_1.rect.y + cube_btn_1.height:
                    LEVEL[0].cube.image = pygame.transform.scale(pygame.image.load('cube-1.png'),
                                                                 (LEVEL[0].cube.radius * 2, LEVEL[0].cube.radius * 2))
                    CUBE_IMAGE = 'cube-1.png'
                elif cube_btn_2.rect.x <= event.pos[0] <= cube_btn_2.rect.x + cube_btn_2.width and \
                        cube_btn_2.rect.y < event.pos[1] < cube_btn_2.rect.y + cube_btn_2.height:
                    LEVEL[0].cube.image = pygame.transform.scale(pygame.image.load('cube-2.png'),
                                                                 (LEVEL[0].cube.radius * 2, LEVEL[0].cube.radius * 2))
                    CUBE_IMAGE = 'cube-2.png'
                elif cube_btn_3.rect.x <= event.pos[0] <= cube_btn_3.rect.x + cube_btn_3.width and \
                        cube_btn_3.rect.y < event.pos[1] < cube_btn_3.rect.y + cube_btn_3.height:
                    LEVEL[0].cube.image = pygame.transform.scale(pygame.image.load('cube-3.png'),
                                                                 (LEVEL[0].cube.radius * 2, LEVEL[0].cube.radius * 2))
                    CUBE_IMAGE = 'cube-3.png'


        if GAME_STATUS == 'CHOOSE_LEVEL':
            choose_lvl_screen.render()

        if GAME_STATUS == 'PAUSE':
            pause_screen.render()

        if GAME_STATUS == 'LEVEL':
            LEVEL[0].start()
            LEVEL[0].update()

            if not LEVEL[0].is_start:
                update_fields()
                if LEVEL[1] == 1:
                    level1 = Level(cube1, surface1, field1, background, screen, 11, jbfield1, jumperField1, 'gd1.mp3')
                    LEVEL[0] = level1
                elif LEVEL[1] == 2:
                    level2 = Level(cube2, surface2, field2, background, screen, 11, jbfield2, jumperField2, 'gd1.mp3')
                    LEVEL[0] = level2
                elif LEVEL[1] == 3:
                    level3 = Level(cube3, surface3, field3, background, screen, 11, jbfield3, jumperField3, 'gd3.mp3')
                    LEVEL[0] = level3
                LEVEL[0].music.start()
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()