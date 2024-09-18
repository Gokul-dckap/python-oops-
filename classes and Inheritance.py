# Classes

# In a Car class, start_engine and drive could be methods. “
# class car:
#     def __init__(self,color,model):
#         self.color = color
#         self.model = model
#
#     def start_engine(self):
#         print("Engine Started!")
#
#     def drive(self):
#         print(f"{self.color.capitalize()} {self.model} is now moving!")
#
# car1 = car("red","Toyota Fortuner",)

# car1.start_engine()
# car1.drive()
#
# car("blue","Tata").drive()


# Another Example of Class with Class Attribute

class Employee:
    raise_amount = 1.04
    def __init__(self,first_name,last_name,email,pay):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.pay = pay

    def fullname(self):
        return "{} {}".format(self.first_name,self.last_name)

    def appraisal(self):
        return int(self.pay * self.raise_amount)

emp1 = Employee("Gokulapriyan","B","gokul@gmail.com",25000)

# print(emp1.fullname())
# print(Employee.fullname(emp1)) # we can print like this also
#
# print(emp1.appraisal())

# print(emp1.__dict__) # convert the parameters and arguments in dictionar
# print(Employee.__dict__) # we can also print like this

                                        # Class Methods
# The @classmethod decorator in Python is used to define a method that is bound to the class rather than the instance of the class.
# It is often used in class-level operations or to create alternative constructors.

# class Person:
#     count_of_people = 0 # Class attribute
#
#     def __init__(self,name):
#         self.name = name
#         Person.add_people()
#
#     # This method doesn't access any sepcific instance,
#     # it only access these class attributes or anything  to the class itself
#     @classmethod
#     def no_of_people(cls):
#         return cls.count_of_people
#
#     @classmethod
#     def add_people(cls):
#         cls.count_of_people += 1
#
# p1 = Person("Gokul")
# p1 = Person("Jeeva")
#
# print(p1.no_of_people())


                                                #Static Method
# Not bound to the class or instance: Static methods don't receive any implicit first argument (like self or cls).
# They behave like regular functions but reside inside a class’s namespace.
# Use case: Static methods are used when you need functionality that doesn't depend on class or instance-specific data but logically relates to the class.
#
# class Math:
#     @staticmethod
#     def add(x,y):
#         print(x+y)
#
# Math.add(5,10)


                                                    #Inheritance
# Inheritance is the concept in OOPs in which one class inherits the attributes and methods of another class.
# The class with inherited properties and methods is known as the Parent class.
# The class that inherits the properties from the parent class is the Child class.
# There are different types of inheritance.

# Single Inheritance

# Parent class or Base class
# class Vehicle:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model
#
#     def start(self):
#         print(f"{self.brand} {self.model} is starting!")
#
#
# class Car(Vehicle):
#     def __init__(self, brand, model, fuel_type):
#         # Using super() to call the parent class's constructor
#         super().__init__(brand,model)
#         self.fuel_type = fuel_type
#
#     # Overriding the parent class's start method
#     def start(self):
#         # Call the parent class's start method using super()
#         super().start()
#         print(f"{self.brand} {self.model} runs on {self.fuel_type}.")
#
# car = Car("Toyota", "Corolla", "Petrol")
#
# car.start()



                                            # Multilevel Class
# In Python, multiple inheritance is when a class can inherit from more than one parent class.

# Parent Class 1
# class Engine:
#     def __init__(self, engine_type):
#         self.engine_type = engine_type
#
#     def start_engine(self):
#         print(f"{self.engine_type} is starting!!")
#
# # Parent Class 2
# class Vehicle:
#     def __init__(self,brand,model):
#         self.brand = brand
#         self.model = model
#
#     def start_vehicle(self):
#         print(f"{self.brand} {self.model} is starting!")
#
# # Child class
# class Car(Engine, Vehicle):
#     def __init__(self, engine_type, brand, model, fuel_type):
#         # Using super() in multiple inheritance
#         super().__init__(engine_type)  # This will call Engine's __init__ method
#         # Engine.__init__(self,engine_type)
#         Vehicle.__init__(self,brand, model)
#         self.fuel_type = fuel_type
#
#     # Overriding method from both parents
#     def start(self):
#         # calling the Parents class methods
#         super().start_engine()  # Using super() to call Engine's method
#         # self.start_engine()
#         self.start_vehicle()
#         print(f"{self.brand} {self.model} runs on {self.fuel_type}.")
#
# # Creating an instance of the child class
# my_car = Car("V8", "Ford", "Mustang", "Petrol")
#
# my_car.start()


                                    # Multilevel Inheritance in Python
# In multilevel inheritance, a class inherits from a parent class, and then another class inherits from that child class.
# It creates a hierarchy of classes, where one class is derived from another in multiple levels.

# GrandParent Class
# class Vehicle:
#     def __init__(self, brand):
#         self.brand = brand
#
#     def start(self):
#         print(f"{self.brand} is starting!!!")
#
# # Intermediate class (parent)
# class car(Vehicle):
#     def __init__(self,brand, model):
#         # Call the constructor of the base class (Vehicle)
#         super().__init__(brand)
#         self.model = model
#
#     # Overriding the start method
#     def start(self):
#         super().start()
#         print(f"{self.model} car is ready to go!")
#
# # Derived class (child)
# class ElectricalCar(car):
#     def __init__(self, brand, model, battery_size):
#         # Call the constructor of the parent class (Car)
#         super().__init__(brand,model)
#         self.battery_size = battery_size
#
#     # Overriding the start method again
#     def start(self):
#         super().start() # Call the parent's start method
#         print(f"{self.model} with a {self.battery_size} kWh battery is now running silently!")
#
# tesla = ElectricalCar("Tesla", "Model s", 100)
#
# tesla.start()

