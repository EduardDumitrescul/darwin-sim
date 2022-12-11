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

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.display.fill(WHITE)

            self.game_data.spriteGroup.draw(self.display)

            pygame.display.flip()
            clock.tick(10)
