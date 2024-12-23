

# Integer to String
age = 25
age_str = str(age)  # Convert int to string
print("Age as a string:", age_str)  # Output: Age as a string: 25


# String to Integer
age_str = "25"
age_int = int(age_str)  # Convert string to int
print("Age plus 5:", age_int + 5)  # Output: Age plus 5: 30


# Float to Integer
price = 19.99
price_int = int(price)  # Convert float to int (truncates decimal)
print("Price as integer:", price_int)  # Output: Price as integer: 19


# Integer to Float
quantity = 10
quantity_float = float(quantity)  # Convert int to float
print("Quantity as float:", quantity_float)  # Output: Quantity as float: 10.0


# List to Tuple
fruits = ["apple", "banana", "cherry"]
fruits_tuple = tuple(fruits)  # Convert list to tuple
print("Fruits as tuple:", fruits_tuple)  # Output: Fruits as tuple: ('apple', 'banana', 'cherry')


# Tuple to List
coordinates = (10.5, 20.7)
coordinates_list = list(coordinates)  # Convert tuple to list
coordinates_list.append(30.2)
print("Coordinates as list:", coordinates_list)  # Output: Coordinates as list: [10.5, 20.7, 30.2]


# String to List
sentence = "Hello World"
words_list = sentence.split()  # Convert string to list by splitting
print("Words as list:", words_list)  # Output: Words as list: ['Hello', 'World']


# List to String
words = ["Hello", "World"]
sentence = " ".join(words)  # Convert list to string by joining
print("Sentence:", sentence)  # Output: Sentence: Hello World
