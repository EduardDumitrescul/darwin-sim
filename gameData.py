import math
from random import random

import pygame.sprite

import entityModel
from entityModel import Entity


class GameData:
    def __init__(self, world_width, world_height, entity_count=20):
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

    def move_entities(self):
        for i in range(0, len(self.entity_list)):
            entity = self.entity_list[i]
            while True:
                angle = random() * 2 * math.pi
                x = entity.rect.x + entity.speed * math.cos(angle)
                y = entity.rect.y + entity.speed * math.sin(angle)
                if 0 <= x <= self.world_width - 2 * entityModel.ENTITY_RADIUS and \
                        0 <= y <= self.world_height - 2 * entityModel.ENTITY_RADIUS:
                    entity.rect.move_ip(entity.speed * math.cos(angle), entity.speed * math.sin(angle))
                    break
