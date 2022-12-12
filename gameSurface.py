import pygame.surface

WHITE = (255, 255, 255)
DEBUG = (255, 100, 255)
class GameSurface(pygame.surface.Surface):
    def __init__(self, width, height, game_data):
        super().__init__([width, height])

        self.width = width
        self.height = height
        self.game_data = game_data

        self.fill(DEBUG)

    def update(self):
        self.fill(DEBUG)
        for entity in self.game_data.entity_list:
            self.blit(entity.image, entity.rect)
