import math
from random import random

import pygame.sprite

import entityModel
import foodModel
from entityModel import Entity


class GameData:
    def __init__(self, world_width, world_height, entity_count=10):
        self.world_width = world_width
        self.world_height = world_height
        self.entity_count = entity_count

        self.food_sprite_group = pygame.sprite.Group()
        self.food_entity_list = []
        self.food_count_limit = 10
        self.food_spawn_rate = 10  # 1 every 10 ticks
        self.food_spawn_last_tick = -1e9

        self.spriteGroup = pygame.sprite.Group()
        self.entity_list = []

        self.create_entities()

        self.in_bounds = lambda x, y: 0 <= x <= self.world_width - 2 * entityModel.ENTITY_RADIUS and \
                                      0 <= y <= self.world_height - 2 * entityModel.ENTITY_RADIUS

    def create_entities(self):
        for i in range(self.entity_count):
            ent = Entity(pos=(random() * (self.world_width - 2 * entityModel.ENTITY_RADIUS),
                              random() * (self.world_height - 2 * entityModel.ENTITY_RADIUS)))
            self.spriteGroup.add(ent)
            self.entity_list.append(ent)

    def update(self, current_tick):
        if current_tick - self.food_spawn_last_tick > self.food_count_limit > len(self.food_entity_list):
            self.food_spawn_last_tick = current_tick
            self.create_food_entity()

    def create_food_entity(self):
        food_entity = foodModel.FoodModel(pos=(random() * (self.world_width - 2 * foodModel.RADIUS),
                                               random() * (self.world_height - 2 * foodModel.RADIUS)))
        self.food_entity_list.append(food_entity)
        self.food_sprite_group.add(food_entity)

    def move_entities(self, delta_time):
        for i in range(len(self.entity_list)):
            entity = self.entity_list[i]
            relative_pos = entity.vector.get_relative_pos(delta_time)
            x = entity.x + relative_pos[0]
            y = entity.y + relative_pos[1]
            if self.in_bounds(x, y):
                entity.x, entity.y = x, y
                entity.rect.x, entity.rect.y = entity.x, entity.y
            else:
                entity.vector.direction = 2 * math.pi * random()

    def compute_path(self):
        for i in range(len(self.entity_list)):
            entity = self.entity_list[i]
            enemy_angle_sum = 0
            enemy_count = 0
            for j in range(0, len(self.entity_list)):
                if i == j:
                    continue

                enemy = self.entity_list[j]
                if entity.distance(enemy) > entity.vision:
                    continue

                enemy_angle_sum += entity.angle(enemy)
                enemy_count += 1

            if enemy_count == 0:
                self.choose_random_path(entity)
                continue

            enemy_angle_sum /= enemy_count
            entity.vector.direction = (enemy_angle_sum + math.pi) % (2 * math.pi)

    def choose_random_path(self, entity):
        vector = entity.vector.get_random_direction()
        x, y = entity.rect.x, entity.rect.y
        xp, yp = vector.get_relative_pos(1 / 10)
        if self.in_bounds(x + xp, y + yp):
            entity.vector = vector
        else:
            vector.direction = 2 * math.pi * random()

        entity.vector = vector

    def check_entity_clicked(self, mouse_pos):
        for entity in self.entity_list:
            if entity.rect.collidepoint(mouse_pos):
                entity.set_selected(True)
            else:
                entity.set_selected(False)
