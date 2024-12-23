

# Things to note:
#  Run and Debug - Debug Toolbar appears top center
#  Step Over and Step Into - same as other debuggers
#  Varibles and Watch areas in left menu
# Can hover over variables to see their value


# Numeric Variables
integer_var = 10                 # Integer
float_var = 3.5                  # Float
complex_var = 2 + 3j             # Complex number
print(f"Integer: {integer_var}, Float: {float_var}, Complex: {complex_var}")



# For loop - Basic iteration over a range of numbers
print("For loop example:")
for i in range(5):  # Iterates from 0 to 4
    print("Iteration:", i)



# Arithmetic Operators
sum_var = integer_var + float_var
difference_var = integer_var - float_var
product_var = integer_var * float_var
quotient_var = integer_var / float_var
power_var = integer_var ** 2     # Exponentiation
modulus_var = integer_var % 3    # Modulus (remainder)
print(f"Sum: {sum_var}, Difference: {difference_var}, Product: {product_var}, Quotient: {quotient_var}, Power: {power_var}, Modulus: {modulus_var}")



# Strings and Concatenation
string_var1 = "Funny"
string_var2 = "Thing"
concatenated_string = string_var1 + " " + string_var2
repeated_string = string_var1 * 3
print(f"Concatenated String: {concatenated_string}, Repeated String: {repeated_string}")



# String Interpolation
name = "Maximus"
age = 25
greeting = f"Hello, my name is {name} and I am {age} years old."
print(greeting)



# Boolean Variables and Comparison Operators
is_sunny = True
is_rainy = False
is_equal = integer_var == 10
is_greater = float_var > 2
print(f"Is it sunny? {is_sunny}, Is it rainy? {is_rainy}")
print(f"Is equal to 10: {is_equal}, Is greater than 2: {is_greater}")



# Logical Operators
and_operation = is_sunny and is_rainy
or_operation = is_sunny or is_rainy
not_operation = not is_rainy
print(f"AND operation: {and_operation}, OR operation: {or_operation}, NOT operation: {not_operation}")



# List Variables and List Operations
list_var = [1, 2, 3, 4, 5]
list_var.append(6)           # Add an element
list_var[0] = 10             # Update first element
list_sum = sum(list_var)     # Sum of list elements
print(f"List: {list_var}, Sum of List: {list_sum}")



# Tuple Variables (Immutable)
tuple_var = (1, 2, 3, 4)
print(f"Tuple: {tuple_var}")



# Dictionary Variables and Dictionary Operations
dict_var = {"name": "Alice", "age": 25, "city": "New York"}
dict_var["age"] = 26                     # Update a value
dict_var["country"] = "USA"              # Add new key-value pair
print(f"Dictionary: {dict_var}")




# Loop Variables
for i in range(5):                       # Loop variable
    print(f"Loop iteration {i}")



# Function with Variables
def greet_user(username):
    return f"Hello, {username}!"

print(greet_user("Alice"))
