

import csv

# parameters
output_filelocation ="/Users/kevinaikens/Desktop/Training/Python/Raw/dogs.csv"


class Dog:

  # The __init__ method is a special method that initializes the object. It’s like the setup for each new object you create. 
  # Here, you set initial values (attributes) for each object.  
    
    def __init__(whodat, name="", age=0, breed="unknown"):   # name defaults to empty string - age is not required if set a default
        whodat.name = name      # Attribute for the dog's name
        whodat.age = age        # Attribute for the dog's age
        whodat.breed = breed    # Attribute for the dog's breed

    # self refers to the current object being created, so self.name and self.age belong to that specific dog.


  # Methods are functions that belong to a class and typically act on the data of that class. Let’s add a method for the dog to "speak."

    def speak(whodat):
        return f"{whodat.name} says Woof!"
    

    def get_age(whodat):
        return f"{whodat.name} is {whodat.age} years old."
    

    def get_breed(whodat):
        return f"The dog is clearly a {whodat.breed} breed."


#   @staticmethod allows save_dogs_to_csv to be used without needing a specific instance of Dog (just a list of any Dog instances).
    @staticmethod
    def save_dogs_to_csv(dogs, filename=output_filelocation):
        # Define the CSV header
        header = ["Name", "Age", "Breed"]

        # Open the CSV file in write mode
        with open(filename, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(header)  # Write header
            for dog in dogs:
                writer.writerow([dog.name, dog.age, dog.breed])  # Write each dog's data

        


# Now that you have a Dog class, you can create specific dog objects:

# Wrap any test or setup code in the following block
# Code inside this block will only run when dog_module.py is executed directly as the main script, not when it’s imported. 
#  This prevents any test code, setup code, or print statements from running in export_dogs.py or any other script that imports Dog.
# Basically, when I call this file and import Dog from another python script - it will not print all the below stmts - Otherwise, it would
if __name__ == "__main__":

    dog1 = Dog("Buddy", 3)
    dog2 = Dog("Luna", 5)
    dog3 = Dog("scooby",7,"ScoobyDoo")

    print(dog1.speak())             # Outputs: Buddy says Woof!
    print(dog2.speak())             # Outputs: Luna says Woof!

    print(Dog("Buddy", 3).speak())  # Outputs: Buddy says Woof!
    print(Dog("Buddy").speak())     # Outputs: Buddy says Woof!

    print(Dog().speak())            # Outputs:  says Woof!

    print(Dog().get_breed())
    print(dog3.get_breed())

    print(Dog(breed="ScoobyDooooooo").get_breed())

    print(Dog(name="Wilma", age=8).get_age())


    print((Dog(name="Wilma", age=8).get_age()), (Dog(breed="ScoobyDooooooo").get_breed()))




# call method to print results to csv
    Dog.save_dogs_to_csv([dog1,dog2,dog3])

