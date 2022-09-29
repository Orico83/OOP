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
        return self.side

    def set_side(self, side):
        self.side = side

    def set_length(self, length):
        super().length = length
        super().width = length

    def set_width(self, width):
        super().length = width
        super().width = width

