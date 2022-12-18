from pygame.font import Font

from uiComponents import linearLayout
from uiComponents.linearLayout import LinearLayout

WHITE = (255, 255, 255)
BLACK = (30, 30, 30)


class FoodInfoSurface(LinearLayout):
    def __init__(self, size, food):
        super().__init__(size, linearLayout.VERTICAL)
        self.food = food

        self.draw_text()

    def draw_text(self):
        font = Font('resources/OpenSans-Regular.ttf', 20)
        text_targeted = font.render(f'trageted by = {self.food.targeted_by}', True, BLACK, WHITE)
        self.add_surface(text_targeted)
