
# Basic Concept:

# Question: What is a class in Python, and how do you define and create an instance of a class?
# Example: Define a simple class called Dog with an __init__ method that initializes the dog's name and age. Create an instance of this class and print its attributes.
# Methods and Behavior:


# Define the class
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Create an instance of the class
my_dog = Dog("Buddy", 3)

# Print attributes
print(f"Name: {my_dog.name}, Age: {my_dog.age}")




# what does it mean to "create an instance of the class"

# Creating an instance of a class is like using a blueprint to build a specific toy based on that blueprint.

# Let’s break it down with a simple example:

# Class Blueprint: Think of a class as a detailed drawing or a recipe for making something. For example, you have a blueprint for a toy car that includes details like its color and size.

# Creating an Instance: When you use the blueprint to actually make a toy car, that specific toy car is called an instance of the class. Each instance is a separate and unique toy car that follows the same blueprint but can have different details (like color or size).

# Here's an analogy:

# Class Blueprint: The class is like a set of instructions for making toy cars.
# Instance: Each toy car you make from these instructions is an instance. Each toy car (instance) can be different in terms of color and size but they all follow the same instructions.
# In Python code:

# Define the class (blueprint) for a toy car
# Define the class (blueprint) for a toy car

class ToyCar:
    def __init__(self, color, size):
        self.color = color
        self.size = size

    def drive(self):
        return "Vroom vroom!"  # Changed from print to return so can be used below in string output/print

# Create an instance (specific toy car) from the blueprint
red_car = ToyCar("red", "small")

# Print the output with the corrected line
print(f"{red_car.color} car time is here. The size of the car is: {red_car.size}. And it goes: {red_car.drive()}")


# Add Age to the ToyCar class to see if the car is new or old

class ToyCar:
    def __init__(self, color, size, age):
        self.color = color
        self.size = size
        self.age = age

    def drive(self):
        return "Vroom vroom!"  # Changed from print to return so can be used below in string output/print

    def age_desc(self):
        if self.age < 2: return 'NEW'
        if self.age == 2 and self.age <=5: return 'average'
        else: return 'OLD'

# Create an instance (specific toy car) from the blueprint
red_car = ToyCar("red", "small", 1)

# Print the output with the corrected line
print(f"{red_car.color} car time is here. The size of the car is: {red_car.size}. This car's age is considered {red_car.age_desc()}. And it goes: {red_car.drive()}")




# Question: How do you add methods to a class to define its behavior, and how can you call these methods on an instance?
# Example: Extend the Dog class from the previous question to include a method called bark that prints a message. Create an instance of Dog and call the bark method.
# Inheritance:

# Question: What is inheritance in Python, and how do you create a subclass that inherits from a parent class?
# Example: Create a subclass Bulldog that inherits from the Dog class. Add an additional attribute called breed and override the bark method to include the breed in the message.
# Encapsulation:

# Question: How can you use encapsulation to protect the internal state of an object and provide controlled access to it?
# Example: Modify the Dog class to include private attributes for name and age. Provide getter and setter methods to access and modify these attributes while keeping them protected from direct external modification.
# Polymorphism and Method Overriding:

# Question: What is polymorphism, and how do you override methods in a subclass to provide specialized behavior?
# Example: Create a base class Animal with a method make_sound. Create two subclasses, Cat and Dog, that override make_sound to provide different implementations. Demonstrate polymorphism by creating a list of Animal objects and calling make_sound on each.



