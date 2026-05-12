"""
Open/Closed Principle (OCP)
---------------------------
Software entities (classes, modules, functions, etc.) should be open for extension, 
but closed for modification.
"""

from abc import ABC, abstractmethod

# VIOLATION: If we add a new shape, we must modify the AreaCalculator class.
class RectangleViolation:
    def __init__(self, width, height):
        self.width = width
        self.height = height

class CircleViolation:
    def __init__(self, radius):
        self.radius = radius

class AreaCalculatorViolation:
    def calculate(self, shapes):
        total_area = 0
        for shape in shapes:
            if isinstance(shape, RectangleViolation):
                total_area += shape.width * shape.height
            elif isinstance(shape, CircleViolation):
                total_area += 3.14 * (shape.radius ** 2)
        return total_area


# ADHERENCE: We can add new shapes by creating new classes without modifying existing code.
class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self) -> float:
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self) -> float:
        return 3.14 * (self.radius ** 2)

class AreaCalculator:
    def calculate(self, shapes: list[Shape]) -> float:
        return sum(shape.area() for shape in shapes)

if __name__ == "__main__":
    shapes = [Rectangle(10, 5), Circle(7)]
    calculator = AreaCalculator()
    print(f"Total Area: {calculator.calculate(shapes)}")
