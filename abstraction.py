#                                          #Abstraction
# """.
# Abstraction is a fundamental concept in Python programming that allows us to simplify complex concepts and focus on the essential details.
# It involves hiding unnecessary details and exposing only the relevant information to the users
# In Python, this is commonly achieved through abstract base classes (using the abc module).
# """
#
#                                         #Abstract Method
# """
# Abstract methods are methods that are declared in a base class but not defined.
# They act as placeholders that must be overridden by subclasses that inherit from the base class.
# Abstract methods enforce a consistent interface for subclasses and ensure that they provide their own implementation of the method.
# """
#
#
# # Example: Abstract Base Class
#
# from abc import ABC, abstractmethod
#
# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass
#
#     @abstractmethod
#     def perimeter(self):
#         pass
#
# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius
#
#     def area(self):
#         return 3.14 * self.radius ** 2
#
#     def perimeter(self):
#         return 2 * 3.14 * self.radius
#
# class Square(Shape):
#     def __init__(self, side):
#         self.side = side
#
#     def area(self):
#         return self.side ** 2
#
#     def perimeter(self):
#         return 4 * self.side
#
# # Instantiate object
# circle1 = Circle(5)
# square1 = Square(4)
#
# print(f"Circle Area: {circle1.area()}")          # Output: Circle Area: 78.5
# print(f"Square Perimeter: {square1.perimeter()}")  # Output: Square Perimeter: 16
#
#
# """
# Explanation:
# The Shape class is an abstract base class, meaning it cannot be instantiated directly.
# Its methods, area() and perimeter(),
# are abstract and must be implemented by any class that inherits from it (e.g., Circle and Square).
# """