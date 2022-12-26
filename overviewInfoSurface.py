import time

from pygame.font import Font

from uiComponents import linearLayout
from uiComponents.linearLayout import LinearLayout

WHITE = (255, 255, 255)
BLACK = (30, 30, 30)


class OverviewInfoSurface(LinearLayout):
    def __init__(self, size, game_data):
        super().__init__(size, linearLayout.VERTICAL)
        self.game_data = game_data

        self.draw_text()

    def draw_text(self, tick=0):
        font = Font('resources/OpenSans-Regular.ttf', 16)

        text_tick = font.render(f'ticks: {self.game_data.current_tick}', True, BLACK, WHITE)
        self.add_surface(text_tick)
        text_time_passed = font.render(f'timer: {time.time() - self.game_data.start_time}s', True, BLACK, WHITE)
        self.add_surface(text_time_passed)
        text_entity_count = font.render(f"entity count: {len(self.game_data.entity_sprite_group)}", True, BLACK, WHITE)
        self.add_surface(text_entity_count)
        text_total_food_collected = font.render(f'total food: {self.game_data.total_food_collected}', True, BLACK, WHITE)
        self.add_surface(text_total_food_collected)
