import math

from shape import Shape


class Circle(Shape):
    def __init__(self, color='Blue', radius=1):
        super().__init__(color, (radius ** 2) * math.pi, 2 * radius * math.pi)
        self.radius = radius

    def get_radius(self):
        return self.radius
