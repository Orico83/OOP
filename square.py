from rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, color='Blue', side=1):
        super().__init__(color, side, side)
        self.side = side

    def get_side(self):
        return self.side

    def set_side(self, side):
        self.side = side

