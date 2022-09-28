class Shape:
    def __init__(self, color='Blue', area=1, perimeter=1):
        self.color = color
        self.area = area
        self.perimeter = perimeter

    def set_color(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def get_area(self):
        return self.area

    def get_perimeter(self):
        return self.perimeter

    def __str__(self):
        return "color: " + self.color + ", area: " + str(self.area) + ", perimeter: " + str(self.perimeter)
