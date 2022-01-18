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


GAME_STATUS = 'MAIN_SCREEN'


if __name__ == '__main__':
    pygame.mixer.pre_init(44100, -16, 1, 512)
    pygame.init()

    screen = pygame.display.set_mode((1920, 1080))

    background = pygame.image.load('background-1.jpg')
    background = pygame.transform.scale(background, (1920, 1080))

    clock = pygame.time.Clock()

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
                    GAME_STATUS = 'LEVEL1'
                    level.music.start()
                elif choose_btn_2.rect.x <= event.pos[0] <= choose_btn_2.rect.x + choose_btn_2.width and \
                        choose_btn_2.rect.y < event.pos[1] < choose_btn_2.rect.y + choose_btn_2.height:
                    GAME_STATUS = 'LEVEL2'
                elif choose_btn_3.rect.x <= event.pos[0] <= choose_btn_3.rect.x + choose_btn_3.width and \
                        choose_btn_3.rect.y < event.pos[1] < choose_btn_3.rect.y + choose_btn_3.height:
                    GAME_STATUS = 'LEVEL3'

        if GAME_STATUS == 'LEVEL1':
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
                level.music.start()
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()