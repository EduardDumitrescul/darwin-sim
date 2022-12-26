import time

from pygame.font import Font

from entityModel import Entity
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

        if len(self.game_data.entity_sprite_group) == 0:
            return

        avg_speed = 0
        avg_max_health = 0
        avg_vision = 0
        avg_reproduction_threshold = 0
        avg_lifespan = 0
        for entity in self.game_data.entity_sprite_group:
            if type(entity) is not Entity:
                continue
            avg_lifespan += entity.lifespan
            avg_vision += entity.vision
            avg_speed += entity.speed
            avg_max_health += entity.max_health
            avg_reproduction_threshold += entity.reproduction_threshold

        avg_speed /= len(self.game_data.entity_sprite_group)
        avg_lifespan /= len(self.game_data.entity_sprite_group)
        avg_reproduction_threshold /= len(self.game_data.entity_sprite_group)
        avg_vision /= len(self.game_data.entity_sprite_group)
        avg_max_health /= len(self.game_data.entity_sprite_group)

        text_avg_speed = font.render(f'avg speed: {avg_speed}', True, BLACK, WHITE)
        self.add_surface(text_avg_speed)
        text_avg_lifespan = font.render(f'avg life: {avg_lifespan}', True, BLACK, WHITE)
        self.add_surface(text_avg_lifespan)
        text_avg_vision = font.render(f'avg vision: {avg_vision}', True, BLACK, WHITE)
        self.add_surface(text_avg_vision)
        text_avg_reproduction_threshold = font.render(f'avg repro: {avg_reproduction_threshold}', True, BLACK, WHITE)
        self.add_surface(text_avg_reproduction_threshold)
        text_avg_max_health = font.render(f'avg max h: {avg_max_health}', True, BLACK, WHITE)
        self.add_surface(text_avg_max_health)
