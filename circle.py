import math

from shape import Shape

PI = math.pi


class Circle(Shape):

    def __init__(self, color='Blue', radius=1):
        """
        Constructor
        :param color: The circle's color
        :param radius: The circle's radius
        """
        super().__init__(color)
        self.radius = radius

    def get_radius(self):
        return self.radius

    def set_radius(self, radius):
        self.radius = radius

    def get_area(self):
        return self.radius ** 2 * PI

    def get_perimeter(self):
        return self.radius * 2 * PI
