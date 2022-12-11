import pygame

from gameData import GameData

WHITE = (255, 255, 255)


class GameView:
    def __init__(self, display_width, display_height):
        self.game_data = GameData(display_width, display_height)
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
            print(delta_time)
            frame_count += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            print(f'frame {frame_count}')
            if frame_count % 5 == 0:
                self.game_data.compute_path()
            self.game_data.move_entities(delta_time)

            self.display.fill(WHITE)

            for entity in self.game_data.entity_list:
                self.display.blit(entity.image, entity.rect)

            pygame.display.flip()
