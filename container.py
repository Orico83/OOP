"""
Author: Ori Cohen
Date: 06/10/2022
Description: A shapes container that is randomly generated using the function 'generate'.
"""

from rectangle import Rectangle
from square import Square
from circle import Circle
import random

COLORS_LIST = ('Blue', 'Red', 'Yellow', 'Green', 'White')
MAX_SIZE = 20
MIN_SIZE = 1


class Container:
    def __init__(self):
        """
        Constructor
        Creates an empty list
        """
        self.shapes_list = list()

    def generate(self, x):
        """
        Generates an x amount of random shapes (rectangle, square or circle) and adds them to shapes_list.
        Their color will be assigned randomly from COLORS_LIST and their sides/radius sizes will be generated randomly
        from the range MIN_SIZE to MAX_SIZE.
        :param x: The amount of shapes to generate.
        """
        for i in range(x):
            new_shape = random.randint(0, 2)
            color = COLORS_LIST[random.randint(0, len(COLORS_LIST) - 1)]
            if new_shape == 0:
                side = random.randint(MIN_SIZE, MAX_SIZE)
                self.shapes_list.append(Square(color, side))
            elif new_shape == 1:
                length = random.randint(MIN_SIZE, MAX_SIZE)
                width = random.randint(MIN_SIZE, MAX_SIZE)
                while length == width:
                    width = random.randint(MIN_SIZE, MAX_SIZE)
                self.shapes_list.append(Rectangle(color, length, width))
            elif new_shape == 2:
                radius = random.randint(MIN_SIZE, MAX_SIZE)
                self.shapes_list.append(Circle(color, radius))

    def sum_areas(self):
        """
        Calculates the total sum of the areas of the shapes in shapes_list.
        :return: The total sum of the areas.
        """
        areas_sum = 0
        for s in self.shapes_list:
            areas_sum += s.get_area()
        return areas_sum

    def sum_perimeters(self):
        """
        Calculates the total sum of the perimeters of the shapes in shapes_list.
        :return: The total sum of the perimeters.
        """
        perimeters_sum = 0
        for s in self.shapes_list:
            perimeters_sum += s.get_perimeter()
        return perimeters_sum

    def count_colors(self):
        """
        Counts the number of times a shape appears in each color.
        :return: A dictionary with the colors as the keys and the numbers as the values.
        """
        colors_dict = dict.fromkeys(COLORS_LIST, 0)
        for s in self.shapes_list:
            colors_dict[s.get_color()] += 1
        return colors_dict


def check_shapes(shapes_list):
    """
    Checks that every shape in the list is a circle/rectangle/square. (For assertion)
    :param shapes_list: A list of shapes
    :return: True if every shape in the list is a circle/rectangle/square. else False.
    """
    for s in shapes_list:
        if isinstance(s, Circle):
            return True
        elif isinstance(s, Square):
            return True
        elif isinstance(s, Rectangle):
            return True
        else:
            return False


def main():
    my_container = Container()
    my_container.generate(100)
    print("total area:", my_container.sum_areas())
    print("total perimeter:", my_container.sum_perimeters())
    print("colors:", my_container.count_colors())


if __name__ == '__main__':
    test_container = Container()
    test_container.generate(5)
    assert len(test_container.shapes_list) == 5
    assert check_shapes(test_container.shapes_list)
    areas = 0
    for shape in test_container.shapes_list:
        areas += shape.get_area()
    assert test_container.sum_areas() == areas
    perimeters = 0
    for shape in test_container.shapes_list:
        perimeters += shape.get_perimeter()
    assert test_container.sum_perimeters() == perimeters
    main()
