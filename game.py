import tkinter
from random import random

import entity
from entity import Entity

from tkinter import *
from tkinter import ttk


class Game:
    def __init__(self, world_width=1000, world_height=800, max_entity_count=20):
        self.world_width = world_width
        self.world_height = world_height
        self.max_entity_count = max_entity_count
        self.entities = []
        for i in range(self.max_entity_count):
            entity = Entity(x=random() * self.world_width, y=random() * self.world_height)
            self.entities.append(entity)


class GameView:
    def __init__(self, game):
        self.game = game
        self.root = tkinter.Tk()
        self.world_canvas = tkinter.Canvas(self.root, bg='white', height=game.world_height, width=game.world_width)

        self.draw_entities()
        self.world_canvas.pack()
        self.root.mainloop()


    def draw_entities(self):
        for ent in self.game.entities:
            x0 = ent.x - entity.ENTITY_RADIUS
            y0 = ent.y - entity.ENTITY_RADIUS
            x1 = ent.x + entity.ENTITY_RADIUS
            y1 = ent.y + entity.ENTITY_RADIUS
            self.world_canvas.create_oval(x0, y0, x1, y1, fill='blue')

