import pygame
from pygame import Surface
from pygame.font import Font

WHITE = (255, 255, 255)
BLACK = (30, 30, 30)

CELL_HEIGHT = 40
CELL_WIDTH = 40
class GamespeedSurface(Surface):
    def __init__(self):
        super().__init__([5 * CELL_WIDTH, CELL_HEIGHT])

        self.fill(WHITE)

        pygame.font.init()
        font = Font('resources/OpenSans-Regular.ttf', 16)
        x1 = font.render('x1', True, BLACK, WHITE)
        self.rect1 = x1.get_rect(center=(0.5 * CELL_WIDTH, 0.5 * CELL_HEIGHT))
        x2 = font.render('x2', True, BLACK, WHITE)
        self.rect2 = x2.get_rect(center=(1.5 * CELL_WIDTH, 0.5 * CELL_HEIGHT))
        x5 = font.render('x5', True, BLACK, WHITE)
        self.rect5 = x5.get_rect(center=(2.5 * CELL_WIDTH, 0.5 * CELL_HEIGHT))
        x10 = font.render('x10', True, BLACK, WHITE)
        self.rect10 = x10.get_rect(center=(3.5 * CELL_WIDTH, 0.5 * CELL_HEIGHT))
        x100 = font.render('x100', True, BLACK, WHITE)
        self.rect100 = x100.get_rect(center=(4.5 * CELL_WIDTH, 0.5 * CELL_HEIGHT))

        self.blit(x1, self.rect1)
        self.blit(x2, self.rect2)
        self.blit(x5, self.rect5)
        self.blit(x10, self.rect10)
        self.blit(x100, self.rect100)

    def check_mouseclick(self, mouse_pos):
        if self.rect1.collidepoint(mouse_pos):
            return 1
        if self.rect2.collidepoint(mouse_pos):
            return 2
        if self.rect5.collidepoint(mouse_pos):
            return 5
        if self.rect10.collidepoint(mouse_pos):
            return 10
        if self.rect100.collidepoint(mouse_pos):
            return 100
        return None

