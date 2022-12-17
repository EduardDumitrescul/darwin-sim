from pygame import Surface

from entityInfoSurface import EntityInfoSurface
from uiComponents import linearLayout
from uiComponents.linearLayout import LinearLayout

WHITE = (255, 255, 255)
DEBUG = (100, 255, 255)
DEBUG2 = (200, 255, 255)


class GameInfoSurface(Surface):
    def __init__(self, width, height, game_data):
        super().__init__([width, height])

        self.game_data = game_data

        self.fill(WHITE)

    def update(self, entity=None):
        self.fill(WHITE)

        if entity is not None:
            entity_info_surface = EntityInfoSurface([self.get_rect().width, 200], entity)
            self.blit(entity_info_surface, [0, 0])
