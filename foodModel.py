import pygame.sprite

ORANGE = (150, 50, 0)
WHITE = (255, 255, 255)
RADIUS = 10


class FoodModel(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()

        self.x = pos[0]
        self.y = pos[1]

        self.image = pygame.surface.Surface([2 * RADIUS, 2 * RADIUS])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)

        pygame.draw.circle(self.image, ORANGE, (RADIUS, RADIUS), RADIUS)

        self.rect = self.image.get_rect()
        self.rect.move_ip(pos)


