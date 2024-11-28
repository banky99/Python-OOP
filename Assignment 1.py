# Create a class representing anything you like (Marvel superheroes)
class Superhero:
    def __init__(self, name, alias, power):  # Use constructors to initialize each object with unique values
        self.name = name  # Public attribute
        self.alias = alias
        self.power = power

    def use_power(self):  # Add methods to bring the class to life
        print(f"{self.alias} uses their power: {self.power}!")

    def reveal_identity(self):
        print(f"{self.alias}'s real identity is {self.name}.")


# Add an inheritance layer to explore polymorphism or encapsulation
class Avenger(Superhero):  # Subclass of Superhero
    def __init__(self, name, alias, power, role):  # Use constructors to initialize each object with unique values
        super().__init__(name, alias, power)  # Call the constructor of the base class
        self.role = role  # Unique attribute for Avenger

    def use_power(self):  # Explore polymorphism: method overriding
        print(f"{self.alias}, the {self.role}, uses their power: {self.power}!")


# Create objects to demonstrate the functionality
spiderman = Superhero("Peter Parker", "Spider-Man", "Web-slinging")  # Unique values for Superhero
ironman = Avenger("Tony Stark", "Iron Man", "Advanced Tech Suit", "Leader")  # Unique values for Avenger

# Interact with objects
spiderman.use_power()  # Demonstrate the Superhero's method
spiderman.reveal_identity()

ironman.use_power()  # Demonstrate polymorphism: Avenger's overridden method
ironman.reveal_identity()
