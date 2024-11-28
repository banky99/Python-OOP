# Base class for all vehicles
class Vehicle:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method")


# Subclass representing a Car
class Car(Vehicle):
    def move(self):  # Overriding the move method
        print("Driving ")


# Subclass representing a Plane
class Plane(Vehicle):
    def move(self):  # Overriding the move method
        print("Flying ")


# Subclass representing a Boat
class Boat(Vehicle):
    def move(self):  # Overriding the move method
        print("Sailing ")


# Subclass representing a Bicycle
class Bicycle(Vehicle):
    def move(self):  # Overriding the move method
        print("Pedaling ")


# Polymorphism Challenge 🎭
def vehicle_move_challenge(vehicle):
    vehicle.move()  # The move method behaves differently based on the vehicle type


# Create instances of different vehicles
car = Car()
plane = Plane()
boat = Boat()
bicycle = Bicycle()

# Test the polymorphic behavior
print("Polymorphism Challenge! 🎭")
vehicle_move_challenge(car)      # Output: Driving 🚗
vehicle_move_challenge(plane)    # Output: Flying ✈️
vehicle_move_challenge(boat)     # Output: Sailing 🚤
vehicle_move_challenge(bicycle)  # Output: Pedaling 🚲
