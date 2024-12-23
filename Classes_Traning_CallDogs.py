
import csv
from Classes_Training import Dog



# dog1 = Dog("Buddy", 3)
# dog2 = Dog("Luna", 5, "Poodle")
# dog3 = Dog("scooby",7,"ScoobyDoo")


# Create a simple list of Dog instances
dogsList = [
    Dog("Buddy", 3),
    Dog("Luna", 5),
    Dog("Charlie", 2),
    Dog("Bella", 4),
    Dog("Rocky", 1)
]


Dog.save_dogs_to_csv(dogsList)
