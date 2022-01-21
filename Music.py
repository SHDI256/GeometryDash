import pygame


class Music:
    def __init__(self, music):
        self.track = music
        pygame.mixer.music.load(music)
        self.f = True

    def start(self):
        pygame.mixer.music.play(-1) if self.f else pygame.mixer.music.unpause()
        self.f = False

    def stop(self):
        pygame.mixer.music.pause()