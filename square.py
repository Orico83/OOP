"""
Author: Ori Cohen
Date: 06/10/2022
Description: A child class that inherits from Rectangle that represents a square by its color and side, and calculates
its area and perimeter.
"""
from rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, color='Blue', side=1):
        """
        Constructor
        :param color: The square's color
        :param side: The square's side
        """
        super().__init__(color, side, side)
        self.side = side

    def get_side(self):
        """
        :return: The square's side
        """
        return self.side

    def set_side(self, side):
        """
        Set the square's side
        :param side: The size to set the square's side to
        """
        self.side = side
        super().set_length(side)
        super().set_width(side)


def main():
    s = Square("White", 7)
    print(s)


if __name__ == '__main__':
    test_square = Square("Yellow", 3)
    assert test_square.get_color() == "Yellow"
    assert test_square.get_area() == 9
    assert test_square.get_perimeter() == 12
    assert test_square.get_side() == 3
    test_square.set_side(5)
    assert test_square.get_side() == 5
    assert test_square.get_area() == 25
    assert test_square.get_perimeter() == 20
    main()
