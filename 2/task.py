class Circle:
    def __init__(self, radius):
        self.radius = radius
    def get_radius(self):
        return f"Радиус круга: {self.radius}"
    def set_radius(self, new_radius):
        self.radius = new_radius
        return f"Радиус изменён на: {self.radius}"


circle = Circle(3)
print(circle.get_radius())
circle.set_radius(12)
print(circle.get_radius())