import pygame


class Music:
    def __init__(self, music):
        pygame.mixer.music.load(music)

    def start(self):
        pygame.mixer.music.play(-1)

    def stop(self):
        pygame.mixer.music.stop()