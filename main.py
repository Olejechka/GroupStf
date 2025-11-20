import math
from abc import ABC, abstractmethod


# Абстрактный базовый класс для всех геометрических фигур.
# Определяет обязательные методы: площадь и периметр.
class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        pass

    @abstractmethod
    def perimeter(self) -> float:
        pass


# Класс круга: определяется радиусом.
# Реализует площадь (πr²) и периметр (длину окружности: 2πr).
class Circle(Shape):
    def __init__(self, radius):
        if radius <= 0:
            raise ValueError("Радиус должен быть положительным числом.")
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


# Класс треугольника: задаётся тремя сторонами.
# Проверяет корректность сторон через неравенство треугольника.
# Площадь вычисляется по формуле Герона.
class Triangle(Shape):
    def __init__(self, a, b, c):
        if a <= 0 or b <= 0 or c <= 0:
            raise ValueError("Стороны треугольника должны быть положительными.")
        if a + b <= c or a + c <= b or b + c <= a:
            raise ValueError("Недопустимые длины сторон: не выполняется неравенство треугольника.")
        self.a, self.b, self.c = a, b, c

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        s = self.perimeter() / 2  # Полупериметр
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))


# Класс квадрата: определяется длиной одной стороны.
# Площадь = side², периметр = 4 * side.
class Square(Shape):
    def __init__(self, side):
        if side <= 0:
            raise ValueError("Сторона квадрата должна быть положительной.")
        self.side = side

    def area(self):
        return self.side ** 2

    def perimeter(self):
        return 4 * self.side