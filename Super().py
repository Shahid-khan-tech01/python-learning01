# Super() : The function used in a child class to call methods from a parent class (super class).

class Shape:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled

    def describe(self):
        print(f"It is a {self.color} and {'filled' if self.is_filled else 'not filled'}")

class Circle(Shape):
    def __init__(self, radius, color, is_filled):
        super().__init__(color, is_filled)
        self.radius = radius

    def describe(self):
        super().describe()
        print(f"It is a Circle with an area of {3.14 * self.radius * self.radius}cm^2")

class Square(Shape):
    def __init__(self, width, color, is_filled):
        super().__init__(color, is_filled)
        self.width = width

    def describe(self):
        super().describe()
        print(f"It is a Square with an area of {self.width * self.width}cm^2")

class Triangle(Shape):
    def __init__(self, width, height, color, is_filled):
        super().__init__(color, is_filled)
        self.width = width
        self.height = height

    def describe(self):
        super().describe()
        print(f"It is a Triangle with an area of {self.height * self.width / 2}cm^2")


circle = Circle(color="red", is_filled=True, radius=5 )
square = Square(color="blue", is_filled=False, width=7 )
triangle = Triangle(width=7, height=5, color="green", is_filled=False)


print("**********************************")
print()
circle.describe()
print()
print("**********************************")
print()
square.describe()
print()
print("**********************************")
print()
triangle.describe()
print()
print("**********************************")


