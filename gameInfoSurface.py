from pygame import Surface

import linearLayout
from linearLayout import LinearLayout

WHITE = (255, 255, 255)
DEBUG = (100, 255, 255)
DEBUG2 = (200, 255, 255)


class GameInfoSurface(Surface):
    def __init__(self, width, height, game_data):
        super().__init__([width, height])

        self.game_data = game_data

        self.fill(WHITE)

        linear_layout = LinearLayout([100, 100], linearLayout.HORIZONTAL)
        s1 = Surface([20, 20])
        s1.fill(DEBUG)
        s2 = Surface([20, 20])
        s2.fill(DEBUG2)
        linear_layout.add_surface(s1)
        linear_layout.add_surface(s2)

        self.blit(linear_layout, [0, 0])
