

# Dictionary
#  A dictionary in Python is an UNORDERED collection of key-value pairs. Keys are unique and used to access values.


my_dict = {'name': 'Alice', 'age': 25, 'city': 'New York'}

# Access a value
print(my_dict['name'])  # Output: Alice

print(my_dict['age'])  # Output: 25

# Add or update a key-value pair
my_dict['age'] = 26

print(my_dict['age'])  # Output: 26

# Check if a key exists
print('name' in my_dict)  # Output: True




# List
# A list is an ORDERED collection of items that allows duplicates


my_list = [1, 2, 3, 4, 5]

print(my_list)  # prints full list

# Access an item by index
print(my_list[2])  # Output: 3

# Add an item
my_list.append(6)

# Remove an item
my_list.remove(3)

# Print updated list after previous 2 modifications
print(my_list) 





# Queue:
# A queue is a collection that follows the FIFO (First-In-First-Out) principle.


from collections import deque

# Create a queue
queue = deque()

# Add to queue
queue.append(1)  # Enqueue - add elements to the right (last in)
queue.append(2)
queue.append(3)

# Remove from queue
print(queue.popleft())  # Dequeue: Output 1
print(queue.popleft())  # Popleft ensures the first in (left most) is the first out  




# Set:
# A set is an UNORDERED collection of unique elements.

my_set = {1, 2, 3, 4}

# Add an element
my_set.add(5)

# Remove an element
my_set.discard(3)

print(my_set)  # Output: {1, 2, 4, 5}

# Check membership
print(2 in my_set)  # Output: True




# Counter:
# A Counter is a subclass of dict used for counting hashable objects

from collections import Counter

data = ['a', 'b', 'a', 'c', 'b', 'a']

counter = Counter(data)

print(counter)  # Output: Counter({'a': 3, 'b': 2, 'c': 1})
print(counter['a'])  # Output: 3




