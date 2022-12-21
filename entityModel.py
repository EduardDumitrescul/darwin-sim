import math
import random
import sys

import pygame.sprite

from vector2d import Vector2D

ENTITY_RADIUS = 20
WHITE = (255, 255, 255)
COLOR_KEY = (255, 0, 255)

BASE_COLOR = (188, 169, 225)
SELECTED_COLOR = (152, 167, 242)

HEALTH_UPDATE_TICK = 6
HEALTH_GAIN_FROM_FOOD = 20
HEALTH_BASE_LOSS = 1
REPRODUCE_THRESHOLD = 10
REPRODUCE_COST = 6


class Entity(pygame.sprite.Sprite):
    def __init__(self, pos=(0, 0)):
        """

        :param pos: tuple(float, float)
        """
        super().__init__()

        self.max_health = 100
        self.health = 100
        self.health_tick_count = 0
        self.speed = 2.0
        self.vision = 200.0
        self.vector = Vector2D()
        self.food_collected = 0

        self.x = pos[0]
        self.y = pos[1]

        self.image = pygame.Surface([2*ENTITY_RADIUS, 2*ENTITY_RADIUS])
        self.image.fill(COLOR_KEY)
        self.image.set_colorkey(COLOR_KEY)

        pygame.draw.circle(self.image, BASE_COLOR, (ENTITY_RADIUS, ENTITY_RADIUS), ENTITY_RADIUS)

        self.rect = self.image.get_rect()
        self.rect.move_ip(pos)

    def set_selected(self, boolean):
        if boolean:
            pygame.draw.circle(self.image, SELECTED_COLOR, (ENTITY_RADIUS, ENTITY_RADIUS), ENTITY_RADIUS)
        else:
            pygame.draw.circle(self.image, BASE_COLOR, (ENTITY_RADIUS, ENTITY_RADIUS), ENTITY_RADIUS)

    def distance(self, entity):
        if entity is None:
            return sys.maxsize
        return pygame.math.Vector2(self.x, self.y).distance_to((entity.x, entity.y))

    def distance_from_point(self, x, y):
        return pygame.math.Vector2(self.x, self.y).distance_to((x, y))

    def angle(self, entity):
        dx = entity.x - self.x
        dy = entity.y - self.y
        return math.atan2(dy, dx)
