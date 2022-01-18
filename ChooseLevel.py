import pygame


class ChooseLevelScreen:
    def __init__(self, background, btn_1, btn_2, btn_3, screen):
        self.background = pygame.transform.scale(pygame.image.load(background), (1920, 1080))
        self.btn_lvl1 = btn_1
        self.btn_lvl2 = btn_2
        self.btn_lvl3 = btn_3
        self.btns_lvl = pygame.sprite.Group()
        [self.btns_lvl.add(btn) for btn in (self.btn_lvl1, self.btn_lvl2, self.btn_lvl3)]
        self.screen = screen

    def render(self):
        self.screen.blit(self.background, (0, 0))
        self.btns_lvl.draw(self.screen)