class Shape:
    def __init__(self, name):
        self.name = name

    def area(self):
        pass

    def describe(self):
        return f"{self.name} has area {self.area()}"

class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

class Square(Shape):
    def __init__(self, side):
        super().__init__("Square")
        self.side = side

    def area(self):
        return self.side ** 2
