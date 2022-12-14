import pygame

import gameData
from gameData import GameData
from gameInfoSurface import GameInfoSurface
from gameSurface import GameSurface

WHITE = (255, 255, 255)

INFO_SURFACE_WIDTH = 200

FPS = 60
TPS = 12


class GameView:
    def __init__(self, display_width, display_height):
        self.game_data = GameData(display_width - INFO_SURFACE_WIDTH, display_height)
        self.game_surface = GameSurface(display_width - INFO_SURFACE_WIDTH, display_height, self.game_data)
        self.game_surface_pos = (0, 0)

        self.game_info_surface = GameInfoSurface(INFO_SURFACE_WIDTH, display_height, self.game_data)
        self.game_info_surface_pos = (display_width - INFO_SURFACE_WIDTH, 0)

        self.display = None
        self.display_width = display_width
        self.display_height = display_height

        self.setup_pygame()
        self.start_gameloop()

    def setup_pygame(self):
        pygame.init()
        pygame.display.set_caption('Darwin Sim')
        self.display = pygame.display.set_mode([self.display_width, self.display_height])

    def start_gameloop(self):
        clock = pygame.time.Clock()
        running = True

        frame_count = 0

        last_tick_millis = 0
        tick_count = 0

        while running:
            delta_time = clock.tick(60) / 1000
            current_ticks_millis = pygame.time.get_ticks()

            if current_ticks_millis - last_tick_millis > 1000.0 / TPS:
                tick_count += 1
                last_tick_millis = current_ticks_millis
                self.update_logic()

            frame_count += 1

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.game_data.check_entity_clicked(pygame.mouse.get_pos())

            # print(f'frame {frame_count}')

            self.update_view(delta_time)

    def update_logic(self):
        self.game_data.update()
        self.game_data.compute_path()

    def update_view(self, delta_time):
        self.display.fill(WHITE)
        self.game_surface.update()
        self.display.blit(self.game_surface, self.game_surface_pos)
        self.display.blit(self.game_info_surface, self.game_info_surface_pos)

        self.game_data.move_entities(delta_time)

        pygame.display.flip()
