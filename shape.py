from abc import ABC, abstractmethod


class Shape(ABC):

    def __init__(self, color='Blue', area=1, perimeter=1):
        """
        constructor
        :param color: The shape's color
        :param area: The shape's area
        :param perimeter: The shape's perimeter
        """
        self.color = color
        self.area = area
        self.perimeter = perimeter

    def set_color(self, color):
        """
        Set the shapes color
        :param color: The color t set the shape to.
        """
        self.color = color

    def get_color(self):
        """
        :return: The shapes color.
        """
        return self.color

    @abstractmethod
    def get_area(self):
        """
        :return: The shapes area.
        """
        return None

    @abstractmethod
    def get_perimeter(self):
        """
        :return: The shapes perimeter.
        """
        return None

    def __str__(self):
        """

        :return:
        """
        return "color: " + self.color + ", area: " + str(self.area) + ", perimeter: " + str(self.perimeter)
