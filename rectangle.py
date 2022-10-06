"""
Author: Ori Cohen
Date: 06/10/2022
Description: A child class that inherits from Shape and represents a rectangle by its color, length and width, and
calculates its area and perimeter.
The class is also a parent class to Square. Includes a function that combines two rectangles.
"""

from shape import Shape


class Rectangle(Shape):
    def __init__(self, color='Blue', length=1, width=1):
        """
        Constructor
        :param color: The rectangle's color
        :param length:
        :param width:
        """
        super().__init__(color)
        self.length = length
        self.width = width

    def get_length(self):
        """
        :return: The rectangle's length
        """
        return self.length

    def get_width(self):
        """
        :return: The rectangle's width
        """
        return self.width

    def set_length(self, length):
        """
        Set the rectangle's length
        :param length: The length to set the rectangle to
        """
        self.length = length

    def set_width(self, width):
        """
        Set the rectangle's length
        :param width: The width to set the rectangle to
        """
        self.width = width

    def get_area(self):
        """
        :return: The rectangle's area
        """
        return self.length * self.width

    def get_perimeter(self):
        """
        :return: The rectangle's perimeter
        """
        return self.length * 2 + self.width * 2

    def combine_rectangles(self, rect):
        """
        This function combines two rectangles with the same color and one of their sides is equal to one side of the
        other rectangle.
        :param rect: The rectangle to add to self.
        :return: The combined Rectangle
        """
        new_width = 0
        new_length = 0
        if isinstance(rect, Rectangle) and self.color == rect.color:
            if self.width == rect.width:
                new_width = self.width
                new_length = self.length + rect.length
            elif self.length == rect.length:
                new_width = self.width + rect.width
                new_length = self.length
            elif self.length == rect.width:
                new_width = self.width + rect.length
                new_length = self.length
            elif self.width == rect.length:
                new_width = self.width
                new_length = self.length + rect.width
        else:
            return None
        return Rectangle(self.color, new_length, new_width)


def main():
    r = Rectangle("Blue", 4, 7)
    print(r)
    r1 = Rectangle("Blue", 6, 4)
    print(r1)
    n = r.combine_rectangles(r1)
    print(n)


if __name__ == '__main__':
    test_rectangle = Rectangle("Yellow", 3, 8)
    assert test_rectangle.get_color() == "Yellow"
    assert test_rectangle.get_area() == 24
    assert test_rectangle.get_perimeter() == 22
    assert test_rectangle.get_length() == 3
    assert test_rectangle.get_width() == 8
    test_rectangle.set_length(5)
    test_rectangle.set_width(2)
    assert test_rectangle.get_length() == 5
    assert test_rectangle.get_width() == 2
    assert test_rectangle.get_area() == 10
    assert test_rectangle.get_perimeter() == 14
    test_rectangle.set_color("Blue")
    assert test_rectangle.get_color() == 'Blue'
    test_rectangle1 = Rectangle("Red", 3, 2)
    test_rectangle2 = Rectangle("Red", 6, 3)
    new_rectangle = test_rectangle1.combine_rectangles(test_rectangle2)
    assert new_rectangle.get_color() == "Red"
    assert new_rectangle.get_length() == 3
    assert new_rectangle.get_width() == 8
    assert new_rectangle.get_area() == 24
    assert new_rectangle.get_perimeter() == 22
    main()
