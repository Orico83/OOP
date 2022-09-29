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
        self.radius = radius
        super().__init__(color, self.get_area(), self.get_perimeter())
        self.radius = radius

    def get_radius(self):
        """
        :return: The circle's radius
        """
        return self.radius

    def set_radius(self, radius):
        """
        Set the circle's radius
        :param radius: The radius to set the circle to.
        """
        self.radius = radius

    def get_area(self):
        """
        :return: The circle's area
        """
        return self.radius ** 2 * PI

    def get_perimeter(self):
        """
        :return: The circle's perimeter
        """
        return self.radius * 2 * PI


def main():
    c = Circle("Green", 5)
    print(c)


if __name__ == '__main__':
    test_circle = Circle('Red', 10)
    assert test_circle.get_color() == 'Red'
    assert test_circle.get_radius() == 10
    assert test_circle.get_area() == 100 * math.pi
    assert test_circle.get_perimeter() == 20 * math.pi
    main()
