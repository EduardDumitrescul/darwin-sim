import pygame.surface

WHITE = (255, 255, 255)
DEBUG = (100, 255, 255)

WHITE = DEBUG


class GameInfoSurface(pygame.surface.Surface):
    def __init__(self, width, height, game_data):
        super().__init__([width, height])

        self.game_data = game_data

        self.fill(WHITE)
