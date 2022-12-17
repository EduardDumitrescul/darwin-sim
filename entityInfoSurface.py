from pygame.font import Font

from uiComponents import linearLayout
from uiComponents.linearLayout import LinearLayout

WHITE = (255, 255, 255)
BLACK = (30, 30, 30)


class EntityInfoSurface(LinearLayout):
    def __init__(self, size, entity):
        super().__init__(size, linearLayout.VERTICAL)
        self.entity = entity

        self.draw_text()

    def draw_text(self):
        font = Font('resources/OpenSans-Regular.ttf', 20)
        text_vision = font.render(f'vision = {self.entity.vision}', True, BLACK, WHITE)
        self.add_surface(text_vision)
        text_speed = font.render(f'speed = {self.entity.speed}', True, BLACK, WHITE)
        self.add_surface(text_speed)
        text_food_collected = font.render(f"food collected = {self.entity.food_collected}", True, BLACK, WHITE)
        self.add_surface(text_food_collected)
