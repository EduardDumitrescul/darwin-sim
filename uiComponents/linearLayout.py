from pygame import Surface

WHITE = (255, 255, 255)

VERTICAL = 0
HORIZONTAL = 1


class LinearLayout(Surface):
    def __init__(self, size, orientation):
        super().__init__(size)

        self.orientation = orientation
        self.padding_begin = 0
        self.padding_end = 0
        self.padding_top = 0
        self.padding_bottom = 0
        self.surface_list = []

    def set_padding(self, begin, top, end, bottom):
        self.padding_begin = begin
        self.padding_top = top
        self.padding_end = end
        self.padding_bottom = bottom

    def add_surface(self, surface):
        self.surface_list.append(surface)
        self.refresh()

    def refresh(self):
        self.fill(WHITE)
        x, y = self.padding_begin, self.padding_top
        for surface in self.surface_list:
            self.blit(surface, [x, y])
            if self.orientation == VERTICAL:
                y += surface.get_rect().height
            else:
                x += surface.get_rect().width


