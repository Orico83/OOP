from shape import Shape


class Rectangle(Shape):
    def __init__(self, color='Blue', x=1, y=1):
        super().__init__(color)
        self.length = x
        self.width = y

    def get_length(self):
        return self.length

    def get_width(self):
        return self.width
    
    def set_length(self, length):
        self.length = length
        
    def set_width(self, width):
        self.width = width

    def get_area(self):
        return self.length + self.width

    def get_perimeter(self):
        return self.length * 2 + self.width * 2

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

