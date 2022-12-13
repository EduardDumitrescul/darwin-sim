import pygame

import gameData
from gameData import GameData
from gameInfoSurface import GameInfoSurface
from gameSurface import GameSurface

WHITE = (255, 255, 255)

INFO_SURFACE_WIDTH = 200


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

        while running:
            delta_time = clock.tick(60) / 1000
            current_ticks = pygame.time.get_ticks()

            print(current_ticks)
            frame_count += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.game_data.check_entity_clicked(pygame.mouse.get_pos())

            print(f'frame {frame_count}')
            if frame_count % 4 == 0:
                self.game_data.compute_path()
            self.game_data.move_entities(delta_time)

            self.game_data.update(current_ticks)

            self.display.fill(WHITE)

            self.game_surface.update()
            self.display.blit(self.game_surface, self.game_surface_pos)

            self.display.blit(self.game_info_surface, self.game_info_surface_pos)

            # for entity in self.game_data.entity_list:
            #     self.display.blit(entity.image, entity.rect)

            pygame.display.flip()
