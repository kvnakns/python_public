
# Intro
print("Various data types below:")



# Numeric Types
age = 25                       # Integer: whole numbers, positive or negative
price = 19.99                  # Float: decimal numbers
complex_num = 3 + 4j           # Complex: complex numbers with real and imaginary parts
print("Numeric Types:", age, price, complex_num)

# Boolean
is_active = True               # Boolean: True or False values
print("Boolean:", is_active)

# String
name = "Alice"                 # String: sequence of characters
print("String:", name)

# List
fruits = ["apple", "banana", "cherry"]  # List: ordered, mutable collection
print("List:", fruits)

# Tuple
coordinates = (10.5, 20.7)     # Tuple: ordered, immutable collection
print("Tuple:", coordinates)

# Set
unique_numbers = {1, 2, 3, 3}  # Set: unordered collection of unique items
print("Set:", unique_numbers)

# Dictionary
person = {"name": "Alice", "age": 30}   # Dictionary: key-value pairs
print("Dictionary:", person)

# Range
numbers = range(1, 5)          # Range: sequence of numbers (1 to 4 in this case)
print("Range:", list(numbers))

# NoneType
result = None                  # NoneType: represents the absence of a value
print("NoneType:", result)

# Bytes
byte_data = b"Hello"           # Bytes: immutable sequence of bytes
print("Bytes:", byte_data)

# Bytearray
mutable_byte_data = bytearray(b"Hello")  # Bytearray: mutable sequence of bytes
mutable_byte_data[0] = 72
print("Bytearray:", mutable_byte_data)

# Frozenset
frozen_set = frozenset([1, 2, 3, 3])   # Frozenset: immutable version of a set
print("Frozenset:", frozen_set)

# Complex Types
from datetime import datetime, date, time, timedelta

current_date = date.today()    # Date: represents a date
current_time = time(14, 30)    # Time: represents a time
current_datetime = datetime.now()  # Datetime: represents both date and time
time_delta = timedelta(days=5) # Timedelta: represents a duration
print("Complex Types:", current_date, current_time, current_datetime, time_delta)

# MemoryView
data = bytearray("Hello", "utf-8")
memory_view = memoryview(data)  # MemoryView: allows access to the memory of other binary objects
print("MemoryView:", memory_view[0])

# User-Defined Class
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

my_car = Car("Toyota", "Corolla")   # User-defined class type
print("User-Defined Class:", my_car.make, my_car.model)

# Callable (function)
def greet(name):
    return f"Hello, {name}!"

print("Callable (Function):", greet("Alice"))
