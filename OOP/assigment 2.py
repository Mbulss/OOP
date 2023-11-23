from abc import ABC, abstractmethod

# Encapsulation: Using a class to encapsulate data and methods
class Car:
    def __init__(self, brand, model):
        self._brand = brand  # Encapsulated attribute
        self._model = model  # Encapsulated attribute

    def get_car_info(self):
        """Get information about the car."""
        return f"Car Info: {self._brand} {self._model}"

    def set_brand(self, new_brand):
        """Set a new brand for the car."""
        self._brand = new_brand

    def get_brand(self):
        """Get the brand of the car."""
        return self._brand


# Inheritance: Creating a subclass that inherits from a superclass
class SuperCar(Car):
    def __init__(self, brand, model, top_speed):
        super().__init__(brand, model)
        self._top_speed = top_speed

    def get_car_info(self):
        """Get information about the supercar."""
        return f"Super Car Info: {self._brand} {self._model} - Top Speed: {self._top_speed} mph"


# Abstraction: Using abstract classes or methods to hide implementation details
class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass


class Square(Shape):
    def __init__(self, side_length):
        self._side_length = side_length

    def calculate_area(self):
        """Calculate the area of a square."""
        return self._side_length * self._side_length


# Creating instances of Car, SuperCar, and Square classes
car = Car("Mazda", "Mercy")
super_car = SuperCar("Ferrari", "Porsche", 269)
square = Square(5)

# Demonstrating methods from Car class
print(car.get_car_info())  
car.set_brand("")
print(car.get_car_info())  

# Demonstrating methods from SuperCar class
print(super_car.get_car_info())  

# Demonstrating methods from Square class
print(square.calculate_area())  
