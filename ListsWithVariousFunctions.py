

# List of numbers for demonstration
numbers = [5, 10, 15, 20, 25]


# 1. max() - Find the largest number in the list
largest = max(numbers)
print(f"Max: {largest}")  # Output: 25


# 2. min() - Find the smallest number in the list
smallest = min(numbers)
print(f"Min: {smallest}")  # Output: 5


# 3. sum() - Calculate the sum of all numbers in the list
total = sum(numbers)
print(f"Sum: {total}")  # Output: 75


# 4. len() - Get the length of the list
length = len(numbers)
print(f"Length: {length}")  # Output: 5


# 5. sorted() - Return a sorted version of the list (does not modify the original list)
sorted_numbers = sorted(numbers, reverse=True)  # Sorts in descending order
print(f"Sorted: {sorted_numbers}")  # Output: [25, 20, 15, 10, 5]


# 6. any() - Check if any element in the list is True (non-zero or non-empty)
contains_nonzero = any(numbers)
print(f"Any non-zero: {contains_nonzero}")  # Output: True


# 7. all() - Check if all elements in the list are True (non-zero or non-empty)
all_nonzero = all(numbers)
print(f"All non-zero: {all_nonzero}")  # Output: True


# 8. abs() - Get the absolute value of a number
negative_number = -10
absolute_value = abs(negative_number)
print(f"Absolute value: {absolute_value}")  # Output: 10


# 9. round() - Round a floating-point number to a specified number of decimal places
float_number = 3.14159
rounded_value = round(float_number, 2)
print(f"Rounded: {rounded_value}")  # Output: 3.14


# 10. zip() - Combine two lists element-wise into pairs
list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]
zipped_list = list(zip(list1, list2))
print(f"Zipped: {zipped_list}")  # Output: [('a', 1), ('b', 2), ('c', 3)]


# 11. map() - Apply a function to each item in a list
squared_numbers = list(map(lambda x: x**2, numbers))
print(f"Squared: {squared_numbers}")  # Output: [25, 100, 225, 400, 625]


# 12. filter() - Filter items in a list based on a condition
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Even numbers: {even_numbers}")  # Output: [10, 20]


# 13. isinstance() - Check if an object is of a specific type
check_type = isinstance(numbers, list)
print(f"Is numbers a list? {check_type}")  # Output: True


# 14. type() - Return the type of an object
object_type = type(numbers)
print(f"Type of numbers: {object_type}")  # Output: <class 'list'>


# 15. range() - Generate a range of numbers from 1 to 5
range_list = list(range(1, 6))
print(f"Range list: {range_list}")  # Output: [1, 2, 3, 4, 5]


# 16. enumerate() - Get index and value pairs from a list
indexed_list = list(enumerate(numbers))
print(f"Enumerated list: {indexed_list}")  # Output: [(0, 5), (1, 10), (2, 15), (3, 20), (4, 25)]


# 17. reversed() - Reverse the order of a list
reversed_numbers = list(reversed(numbers))
print(f"Reversed: {reversed_numbers}")  # Output: [25, 20, 15, 10, 5]
