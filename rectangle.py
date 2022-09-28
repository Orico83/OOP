from shape import Shape


class Rectangle(Shape):
    def __init__(self, color='Blue', x=1, y=1):
        super().__init__(color, (x * y), (x * 2 + y * 2))
        self.length = x
        self.width = y

    def get_length(self):
        return self.length

    def get_width(self):
        return self.width

    def combine_rects(self, rect):
        new_width = 0
        new_length = 0
        if isinstance(rect, Rectangle):
            if self.width == rect.width:
                new_width = self.width
                new_length = self.length + rect.length
            elif self.length == rect.length:
                new_width = self.width + rect.width
                new_length = self.length
            elif self.width == rect.length:
                new_width = self.width + rect.length
                new_length = self.length
            elif self.length == rect.width:
                new_width = self.width
                new_length = self.length + rect.width
        else:
            return None
        return Rectangle(self.color, new_length, new_width)

