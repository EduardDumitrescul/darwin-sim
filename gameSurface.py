import pygame.surface

from gamespeedSurface import GamespeedSurface

WHITE = (255, 255, 255)
DEBUG = (10, 10, 10)


class GameSurface(pygame.surface.Surface):
    def __init__(self, width, height, game_data):
        super().__init__([width, height])

        self.width = width
        self.height = height
        self.game_data = game_data
        self.gamespeed_surface = GamespeedSurface()

        self.fill(DEBUG)

    def update(self):
        self.fill(DEBUG)
        self.game_data.entity_sprite_group.draw(self)

        self.game_data.food_sprite_group.draw(self)
        self.blit(self.gamespeed_surface, [0, 0])
