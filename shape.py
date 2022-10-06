"""
Author: Ori Cohen
Date: 06/10/2022
Description: A parent class that represents a shape by it's color, area and perimeter.
"""


class Shape:

    def __init__(self, color='Blue'):
        """
        constructor
        :param color: The shape's color
        """
        self.color = color

    def set_color(self, color):
        """
        Set the shapes color
        :param color: The color to set the shape to
        """
        self.color = color

    def get_color(self):
        """
        :return: The shapes color
        """
        return self.color

    def get_area(self):
        """
        :return: The shapes area
        """
        return None

    def get_perimeter(self):
        """
        :return: The shapes perimeter
        """
        return None

    def __str__(self):
        return "color: " + self.color + ", area: " + str(self.get_area()) + ", perimeter: " + str(self.get_perimeter())


def main():
    s = Shape("White")
    print(s)


if __name__ == '__main__':
    test_shape = Shape("Red")
    assert test_shape.get_color() == "Red"
    test_shape.set_color("Blue")
    assert test_shape.get_color() == 'Blue'
    main()
