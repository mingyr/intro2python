class Dog:
    """A simple attempt to model a dog."""
    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age
    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")
    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name} rolled over!")

my_dog = Dog('Willie', 6)
print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")

my_dog.sit()
my_dog.roll_over()
        
        
class Car:
    """A simple attempt to represent a car."""
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    def increment_odometer(self, miles):
        self.odometer_reading += miles
    def fill_gas_tank(self, litre):
        print(f"{litre} gas is added into the tank!")

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    def __init__(self, make, model, year):
        """Initialize attributes of the parent class."""
        super().__init__(make, model, year)
        self.battery_size = 75
    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")
    def fill_gas_tank(self, litre):
        """Electric cars don't have gas tanks."""
        print("This car doesn't need a gas tank!")        

my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()


my_rogue = Car("nissan", "rogue sport", 2018)
print(my_rogue.get_descriptive_name())
my_rogue.fill_gas_tank(50)

my_tesla = ElectricCar("tesla", "model s", 2019)
print(my_tesla.get_descriptive_name())
my_tesla.fill_gas_tank(50)


class MyClass:
    """A simple example class"""
    i = 1.0 # This is a class variable
    def __init__(self):
        self.j = 2.0 # This is a instance variable
    def f(): # This is a class method
        print(f"{MyClass.i}")			
    def g(self): # This is a instance variable 
        print(f"{self.j}")
        

class MyClass:
    "This is a test of a class"
    def __init__(self):
        pass

print(MyClass.__doc__)

def myfunction():
    "This is a test of a function"
    pass

print(myfunction.__doc__)        