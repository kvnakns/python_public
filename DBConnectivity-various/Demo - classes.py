


class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.is_running = False  # Start with the car turned off



    # Method to start the car
    def start(self):
        self.is_running = True
        return f"The {self.year} {self.brand} {self.model} is now running."



    # Method to stop the car
    def stop(self):
        self.is_running = False
        return f"The {self.year} {self.brand} {self.model} has been turned off."
    


    # Method to check if the car is running
    def status(self):
        if self.is_running:
            return f"The {self.year} {self.brand} {self.model} is currently running."
        else:
            return f"The {self.year} {self.brand} {self.model} is currently off."





#Creting and using the class

# Create a new car
car1 = Car("Toyota", "Corolla", 2020)
car2 = Car("Porsche", "911", 2024)

# Start the car
print(car1.start())


# Check the car's status
print(car1.status())


# Stop the car
print(car1.stop())


# Check the car's status again
print(car1.status(), car2.status())
