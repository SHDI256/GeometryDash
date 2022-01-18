import pygame
from Button import *


class MainScreen:
    def __init__(self, background, button_start, screen):
        self.screen = screen
        self.background = pygame.transform.scale(pygame.image.load(background), (1920, 1080))
        self.button_start = button_start
        self.start_btn = pygame.sprite.Group()
        self.start_btn.add(button_start)

    def render(self):
        self.screen.blit(self.background, (0, 0))
        self.start_btn.draw(self.screen)