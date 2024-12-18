# Assignment 1: Design Your Own Class!


class ElectronicDevice:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def power_on(self):
        print(f"The {self.brand} {self.model} is now powered on.")

    def power_off(self):
        print(f"The {self.brand} {self.model} is now powered off.")

# Inherit from ElectronicDevice to create a specific class for Smartphones
class Smartphone(ElectronicDevice):
    def __init__(self, brand, model, storage, camera_resolution):
        super().__init__(brand, model)
        self.storage = storage
        self.camera_resolution = camera_resolution

    def take_photo(self):
        print(f"Taking a photo with {self.camera_resolution} resolution.")

    def install_app(self, app_name):
        print(f"Installing {app_name} on the {self.brand} {self.model}.")

# Create objects for testing
phone1 = Smartphone("Apple", "iPhone 14", "256GB", "12MP")
phone2 = Smartphone("Samsung", "Galaxy S23", "512GB", "50MP")

# Test the methods
phone1.power_on()
phone1.take_photo()
phone1.install_app("Instagram")
phone1.power_off()

phone2.power_on()
phone2.take_photo()
phone2.install_app("Twitter")
phone2.power_off()

# Activity 2: Polymorphism Challenge!


class Vehicle:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method.")

# Define specific vehicle classes
class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

class Boat(Vehicle):
    def move(self):
        print("Sailing 🚤")

# Create objects for testing
vehicles = [Car(), Plane(), Boat()]

# Test polymorphism
for vehicle in vehicles:
    vehicle.move()
