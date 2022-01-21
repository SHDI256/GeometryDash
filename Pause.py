import pygame


class PauseScreen:
    def __init__(self, background, button_start, cube_btn_1, cube_btn_2, cube_btn_3, screen):
        self.screen = screen
        self.background = pygame.transform.scale(pygame.image.load(background), (1920, 1080))
        self.button_start = button_start
        self.btns = pygame.sprite.Group()
        self.btns.add(button_start)
        self.btns.add(cube_btn_1)
        self.btns.add(cube_btn_2)
        self.btns.add(cube_btn_3)

    def render(self):
        self.screen.blit(self.background, (0, 0))
        self.btns.draw(self.screen)
