from pygame import Surface

from entityInfoSurface import EntityInfoSurface
from foodInfoSurface import FoodInfoSurface
from overviewInfoSurface import OverviewInfoSurface
from uiComponents import linearLayout
from uiComponents.linearLayout import LinearLayout

WHITE = (255, 255, 255)
DEBUG = (100, 255, 255)
DEBUG2 = (200, 255, 255)


class GameInfoSurface(LinearLayout):
    def __init__(self, width, height, game_data):
        super().__init__([width, height], orientation=linearLayout.VERTICAL)

        self.game_data = game_data

        self.fill(WHITE)

    def update(self, entity=None, food=None):
        self.surface_list = []
        self.fill(WHITE)
        overview_info_surface = OverviewInfoSurface([self.get_rect().width, 200], self.game_data)
        self.add_surface(overview_info_surface)

        if entity is not None:
            entity_info_surface = EntityInfoSurface([self.get_rect().width, 200], entity)
            self.add_surface(entity_info_surface)
        elif food is not None:
            food_info_surface = FoodInfoSurface([self.get_rect().width, 100], food)
            self.add_surface(food_info_surface)

