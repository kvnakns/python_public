
print("\nFactoral function begin:")

f = 8

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print("Factorial of", f, "is", factorial(f))



print("\nGCD function begin:")

def gcd(a, b):
    """
    Calculate the greatest common divisor (GCD) of two integers using the Euclidean algorithm.

    Parameters:
    - a (int): The first integer.
    - b (int): The second integer.

    Returns:
    - int: The greatest common divisor of a and b.

    Raises:
    - ValueError: If either a or b is not a positive integer.
    """
    if a <= 0 or b <= 0:
        raise ValueError("Both numbers must be positive integers.")

    while b != 0:
        a, b = b, a % b  # Swap a and b, and set b to a % b

    return a




# Declare a couple numbers then use the function
# use with error handling
try:
    num1 = 48
    num2 = 18

    print(f"The GCD of {num1} and {num2} is: {gcd(num1, num2)}")
except ValueError as e:
    print(e)
