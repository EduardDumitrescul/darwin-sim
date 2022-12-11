import math
from random import random

import pygame.sprite

import entityModel
from entityModel import Entity


class GameData:
    def __init__(self, world_width, world_height, entity_count=10):
        self.world_width = world_width
        self.world_height = world_height
        self.entity_count = entity_count
        self.spriteGroup = pygame.sprite.Group()
        self.entity_list = []

        self.create_entities()

    def create_entities(self):
        for i in range(self.entity_count):
            ent = Entity(pos=(random() * (self.world_width - 2 * entityModel.ENTITY_RADIUS),
                              random() * (self.world_height - 2 * entityModel.ENTITY_RADIUS)))
            self.spriteGroup.add(ent)
            self.entity_list.append(ent)

    def move_entities(self, delta_time):
        for i in range(len(self.entity_list)):
            entity = self.entity_list[i]
            relative_pos = entity.vector.get_relative_pos(delta_time)
            entity.x += relative_pos[0]
            entity.y += relative_pos[1]
            entity.rect.x, entity.rect.y = entity.x, entity.y

    def compute_path(self):
        for i in range(0, len(self.entity_list)):
            entity = self.entity_list[i]

            vector = entity.vector.get_random_direction()
            x, y = entity.rect.x, entity.rect.y
            xp, yp = vector.get_relative_pos(1)
            if 0 <= x + xp <= self.world_width - 2 * entityModel.ENTITY_RADIUS and \
                    0 <= y + yp <= self.world_height - 2 * entityModel.ENTITY_RADIUS:
                entity.vector = vector
            else:
                vector.direction = 2 * math.pi * random()

            entity.vector = vector
