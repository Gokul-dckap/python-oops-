                                        # Singleton Pattern
# The Singleton pattern ensures that a class has only one instance and provides a global point of access to it.

# Example: Singleton Pattern

# class Singleton:
#     # Class attribute to hold the one and only instance
#     _instance = None
#
#     # Override the __new__ method, which is responsible for creating a new instance
#     def __new__(cls):
#         # Check if an instance of this class has already been created
#         if cls._instance is None:
#             # If no instance exists, create one using the __new__ method of the superclass (object)
#             cls._instance = super().__new__(cls)
#         # Return the existing (or newly created) instance
#         return cls._instance
#
# # Creating the first instance of Singleton
# singleton1 = Singleton()
#
# # Creating another instance of Singleton (this should return the same instance as singleton1)
# singleton2 = Singleton()
#
# # Check if both variables refer to the same instance (should return True)
# print(singleton1 == singleton2)  # Output: True
