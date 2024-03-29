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
        font = Font('resources/OpenSans-Regular.ttf', 12)
        text_tick_born = font.render(f'tick born = {self.entity.tick_born}', True, BLACK, WHITE)
        self.add_surface(text_tick_born)
        text_health = font.render(f'health = {self.entity.health}', True, BLACK, WHITE)
        self.add_surface(text_health)
        text_vision = font.render(f'vision = {self.entity.vision}', True, BLACK, WHITE)
        self.add_surface(text_vision)
        text_speed = font.render(f'speed = {self.entity.speed}', True, BLACK, WHITE)
        self.add_surface(text_speed)
        text_food_collected = font.render(f"food collected = {self.entity.food_collected}", True, BLACK, WHITE)
        self.add_surface(text_food_collected)

