

# For loop - Basic iteration over a range of numbers
print("For loop example:")
for i in range(5):  # Iterates from 0 to 4
    print("Iteration:", i)



# For loop with list
fruits = ["apple", "banana", "cherry"]
print("\nFor loop with list:")
for fruit in fruits:  # Iterates over each item in the list
    print("Fruit:", fruit)



# For loop with dictionary
person = {"name": "Alice", "age": 30, "city": "New York"}
print("\nFor loop with dictionary:")
for key, value in person.items():  # Iterates over dictionary keys and values
    print(f"{key}: {value}")



# Nested for loop
print("\nNested for loop:")
for i in range(1, 4):  # Outer loop
    for j in range(1, 4):  # Inner loop
        print(f"i={i}, j={j}")



# While loop - Basic usage
count = 0
print("\nWhile loop example:")
while count < 5:  # Loop continues until count reaches 5
    print("Count:", count)
    count += 1



# Infinite while loop with break (stopping condition)
print("\nInfinite while loop with break:")
counter = 0
while True:  # Infinite loop
    print("Counter:", counter)
    counter += 1
    if counter >= 3:  # Breaks when counter reaches 3
        break



# Using continue in a loop
print("\nUsing continue in a loop:")
for num in range(5):
    if num == 2:  # Skip the rest of the code in this iteration when num is 2
        continue
    print("Number:", num)



# Looping with else
print("\nLoop with else clause:")
for i in range(3):
    print("Iteration:", i)
else:
    print("Loop ended without break")



# While loop with else
print("\nWhile loop with else clause:")
n = 0
while n < 3:
    print("N:", n)
    n += 1
else:
    print("While loop ended without break")



# List comprehension with loop
print("\nList comprehension example:")
squares = [x**2 for x in range(5)]  # Creates a list of squares
print("Squares:", squares)



# Dictionary comprehension with loop
print("\nDictionary comprehension example:")
even_odd = {x: "even" if x % 2 == 0 else "odd" for x in range(1, 6)}
print("Even/Odd:", even_odd)



# Using enumerate in a loop
print("\nUsing enumerate in a loop:")
for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")



# Using zip to iterate over multiple sequences
colors = ["red", "yellow", "purple"]
print("\nUsing zip to iterate over multiple sequences:")
for fruit, color in zip(fruits, colors):
    print(f"{fruit} is {color}")



# Looping over a set
unique_numbers = {1, 2, 3, 4}
print("\nLooping over a set:")
for num in unique_numbers:
    print("Number in set:", num)



# Looping over a tuple
coordinates = (10.5, 20.7, 30.2)
print("\nLooping over a tuple:")
for coordinate in coordinates:
    print("Coordinate:", coordinate)
