from shape import Shape
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
        from the range MIN_SIZE to MAX_SIZE
        :param x: The amount of shapes to generate.
        """
        for i in range(x):
            shape = random.randint(0, 2)
            color = COLORS_LIST[random.randint(0, len(COLORS_LIST) - 1)]
            if shape == 0:
                side = random.randint(MIN_SIZE, MAX_SIZE)
                self.shapes_list.append(Square(color, side))
            elif shape == 1:
                length = random.randint(MIN_SIZE, MAX_SIZE)
                width = random.randint(MIN_SIZE, MAX_SIZE)
                while length == width:
                    width = random.randint(MIN_SIZE, MAX_SIZE)
                self.shapes_list.append(Rectangle(color, length, width))
            elif shape == 2:
                radius = random.randint(MIN_SIZE, MAX_SIZE)
                self.shapes_list.append(Circle(color, radius))

    def sum_areas(self):
        """
        Calculates the total sum of the areas of the shapes in shapes_list.
        :return: The total sum of the areas.
        """
        areas_sum = 0
        for shape in self.shapes_list:
            areas_sum += shape.get_area()
        return areas_sum

    def sum_perimeters(self):
        """
        Calculates the total sum of the perimeters of the shapes in shapes_list.
        :return: The total sum of the perimeters.
        """
        perimeters_sum = 0
        for shape in self.shapes_list:
            perimeters_sum += shape.get_area()
        return perimeters_sum

    def count_colors(self):
        """
        Counts the number of  times a
        :return:
        """
        colors_dict = dict.fromkeys(COLORS_LIST, 0)
        for shape in self.shapes_list:
            colors_dict[shape.get_color()] += 1
        return colors_dict


def main():
    my_container = Container()
    my_container.generate(100)
    print("total area:", my_container.sum_areas())
    print("total perimeter:", my_container.sum_perimeters())
    print("colors:", my_container.count_colors())


if __name__ == '__main__':
    main()

