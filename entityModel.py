import math
import random

import pygame.sprite

from vector2d import Vector2D

ENTITY_RADIUS = 20
WHITE = (255, 255, 255)
COLOR_KEY = (255, 0, 255)


class Entity(pygame.sprite.Sprite):
    def __init__(self, pos=(0, 0)):
        """

        :param pos: tuple(float, float)
        """
        super().__init__()

        self.speed = 2.0
        self.vector = Vector2D()

        self.image = pygame.Surface([2*ENTITY_RADIUS, 2*ENTITY_RADIUS])
        self.image.fill(COLOR_KEY)
        self.image.set_colorkey(COLOR_KEY)

        pygame.draw.circle(self.image, pygame.Color("#0000AA"), (ENTITY_RADIUS, ENTITY_RADIUS), ENTITY_RADIUS)

        self.rect = self.image.get_rect()
        self.rect.move_ip(pos)


