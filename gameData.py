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

        self.create_entities()

    def create_entities(self):
        for i in range(self.entity_count):
            ent = Entity(pos=(random() * (self.world_width - 2 * entityModel.ENTITY_RADIUS), random() * (self.world_height - 2 * entityModel.ENTITY_RADIUS)))
            self.spriteGroup.add(ent)


