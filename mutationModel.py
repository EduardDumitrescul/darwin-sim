from random import random

MUTATION_CHANCE = 0.8
MUTATION_STRENGTH = 0.1

class MutationModel:
    def __init__(self):
        self.speed = 1.0
        self.vision = 1.0
        self.max_health = 1.0
        self.reproduction_threshold = 1.0
        self.lifespan = 1.0

    def mutate(self, entity):
        print('mutate')
        # SPEED
        if random() <= MUTATION_CHANCE:
            print('mutation')
            if random() < 0.5:
                self.speed = entity.mutation.speed - MUTATION_STRENGTH
            else:
                self.speed = entity.mutation.speed + MUTATION_STRENGTH

        # VISION
        if random() <= MUTATION_CHANCE:
            if random() < 0.5:
                self.vision = entity.mutation.vision - MUTATION_STRENGTH
            else:
                self.vision = entity.mutation.vision + MUTATION_STRENGTH

        # MAX HEALTH
        if random() <= MUTATION_CHANCE:
            if random() < 0.5:
                self.max_health = entity.mutation.max_health - MUTATION_STRENGTH
            else:
                self.max_health = entity.mutation.max_health + MUTATION_STRENGTH

        #  # REPRODUCTION THRESHOLD
        # if random() <= MUTATION_CHANCE:
        #     if random() < 0.5:
        #         self.reproduction_threshold = entity.mutation.reproduction_threshold - MUTATION_STRENGTH
        #     else:
        #         self.reproduction_threshold = entity.mutation.reproduction_threshold + MUTATION_STRENGTH

          # LIFESPAN
        if random() <= MUTATION_CHANCE:
            if random() < 0.5:
                self.lifespan = entity.mutation.lifespan - MUTATION_STRENGTH
            else:
                self.lifespan = entity.mutation.lifespan + MUTATION_STRENGTH

