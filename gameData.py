import math
import time
from random import random

import pygame.sprite
from pygame.sprite import Group

import entityModel
import foodModel
from entityModel import Entity


class GameData:
    def __init__(self, world_width, world_height, entity_count=10):
        self.world_width = world_width
        self.world_height = world_height
        self.entity_count = entity_count

        self.food_sprite_group = Group()
        self.food_list = []
        self.food_count_limit = 10
        self.food_spawn_rate = 10  # 1 every 10 ticks
        self.food_spawn_last_tick = -1e9

        self.entity_sprite_group = Group()

        self.create_entities()

        self.in_bounds = lambda x, y: 0 <= x <= self.world_width - 2 * entityModel.ENTITY_RADIUS and \
                                      0 <= y <= self.world_height - 2 * entityModel.ENTITY_RADIUS

        self.start_time = time.time()
        self.current_tick = 0
        self.total_food_collected = 0

    def create_entities(self):
        for i in range(self.entity_count):
            ent = Entity(pos=(random() * (self.world_width - 2 * entityModel.ENTITY_RADIUS),
                              random() * (self.world_height - 2 * entityModel.ENTITY_RADIUS)))
            self.entity_sprite_group.add(ent)

    def check_entity_reproduction(self):
        for entity in self.entity_sprite_group:
            if type(entity) is not Entity:
                continue
            if entity.food_collected >= entityModel.REPRODUCE_THRESHOLD:
                entity.food_collected -= entityModel.REPRODUCE_COST
                entity.food_collected //= 2
                new_entity = Entity(pos=(entity.x, entity.y), tick=self.current_tick)
                self.entity_sprite_group.add(new_entity)

    def update(self, tick):
        self.current_tick = tick
        self.check_collisions()
        if self.food_count_limit > len(self.food_sprite_group):
            self.create_food_entity()

        for entity in self.entity_sprite_group:
            if type(entity) is Entity:
                self.update_entity_stats(entity)

        self.check_entity_reproduction()

    def update_entity_stats(self, entity):
        entity.health_tick_count += 1
        if entity.health_tick_count == entityModel.HEALTH_UPDATE_TICK:
            entity.health_tick_count = 0
            entity.health -= entityModel.HEALTH_BASE_LOSS * entity.speed

        if int(entity.food_collected) > 0 and entity.max_health - entity.health >= entityModel.HEALTH_GAIN_FROM_FOOD:
            entity.food_collected -= 1
            entity.health += entityModel.HEALTH_GAIN_FROM_FOOD
            entity.health = min(entity.health, entity.max_health)

        if entity.health <= 0:
            self.entity_sprite_group.remove(entity)

    def check_collisions(self):
        dict_entity_food = pygame.sprite.groupcollide(self.entity_sprite_group, self.food_sprite_group, False, True)
        for ent in dict_entity_food:
            if type(ent) is Entity:
                ent.food_collected += 1
                self.total_food_collected += 1

    def create_food_entity(self):
        food_entity = foodModel.FoodModel(pos=(random() * (self.world_width - 2 * foodModel.RADIUS),
                                               random() * (self.world_height - 2 * foodModel.RADIUS)))
        self.food_sprite_group.add(food_entity)

    def move_entities(self, delta_time):
        for entity in self.entity_sprite_group:
            if type(entity) is not Entity:
                continue
            relative_pos = entity.vector.get_relative_pos(delta_time)
            x = entity.x + relative_pos[0] * entity.speed
            y = entity.y + relative_pos[1] * entity.speed
            if self.in_bounds(x, y):
                entity.x, entity.y = x, y
                entity.rect.x, entity.rect.y = entity.x, entity.y
            else:
                entity.vector.direction = 2 * math.pi * random()

    def compute_path(self):
        for entity in self.entity_sprite_group:
            if type(entity) is not Entity:
                continue
            if not self.choose_path_based_on_enemies(entity):
                if not self.choose_path_to_food(entity):
                    self.choose_random_path(entity)

    def choose_path_based_on_enemies(self, entity):

        return False

        enemy_angle_sum = 0
        enemy_count = 0
        for enemy in self.entity_sprite_group:
            if type(enemy) is not Entity:
                continue
            if enemy == entity:
                continue
            if entity.distance(enemy) > entity.vision:
                continue

            enemy_angle_sum += entity.angle(enemy)
            enemy_count += 1

        if enemy_count == 0:
            return False

        enemy_angle_sum /= enemy_count
        entity.vector.direction = (enemy_angle_sum + math.pi) % (2 * math.pi)

        return True

    def choose_path_to_food(self, entity):
        min_dist = 1e9
        target = None
        for food in self.food_sprite_group:
            if type(food) == foodModel.FoodModel:
                if food.targeted_by is None:
                    if min_dist > entity.distance(food):
                        min_dist = entity.distance(food)
                        target = food
                elif type(food.targeted_by) is Entity:
                    if min_dist > entity.distance(food) and (
                            food.targeted_by.distance(food) > entity.distance(food) or food.targeted_by == entity):
                        min_dist = entity.distance(food)
                        target = food

        if entity.distance(target) > entity.vision:
            return False

        if type(target) is foodModel.FoodModel:
            target.targeted_by = entity

        entity.vector.direction = entity.angle(target)
        return True

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
        selected_entity = None
        for entity in self.entity_sprite_group:
            if type(entity) is not Entity:
                continue
            if entity.rect.collidepoint(mouse_pos):
                entity.set_selected(True)
                selected_entity = entity
            else:
                entity.set_selected(False)

        return selected_entity

    def check_food_clicked(self, mouse_pos):
        selected_food = None
        for food in self.food_sprite_group:
            if type(food) is not foodModel.FoodModel:
                continue
            if food.rect.collidepoint(mouse_pos):
                food.set_selected(True)
                selected_food = food
            else:
                food.set_selected(False)

        return selected_food
