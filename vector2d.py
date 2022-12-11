import math
from random import random

PI = math.pi
WANDER_FRACTION = 0.025


class Vector2D:
    def __init__(self):
        self.direction = 2 * PI * random()
        self.velocity = 100.0

    def get_relative_pos(self, delta_time):
        x = self.velocity * math.cos(self.direction) * delta_time
        y = self.velocity * math.sin(self.direction) * delta_time

        return x, y

    def get_random_direction(self):
        d = 2 * PI * (random() - 0.5)
        vector = Vector2D()
        vector.direction = WANDER_FRACTION * d + self.direction
        if vector.direction < 0:
            vector.direction += 2 * PI
        if vector.direction >= 2 * PI:
            vector.direction -= 2 * PI
        vector.velocity = self.velocity
        return vector
