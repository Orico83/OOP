"""
Author: Ori Cohen
Date: 06/10/2022
Description: A child class that inherits from Shape and represents a circle by its color and radius and calculates its
area and perimeter.
"""

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
        super().__init__(color)
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
    c = Circle("Red", 5)
    print(c)


if __name__ == '__main__':
    test_circle = Circle('Red', 10)
    assert test_circle.get_color() == 'Red'
    assert test_circle.get_radius() == 10
    assert test_circle.get_area() == 100 * math.pi
    assert test_circle.get_perimeter() == 20 * math.pi
    test_circle.set_radius(5)
    assert test_circle.get_radius() == 5
    assert test_circle.get_area() == 25 * math.pi
    assert test_circle.get_perimeter() == 10 * math.pi
    main()
