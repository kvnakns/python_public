

from datetime import datetime



def check_age(age):
    """Check if the person is a child, teenager, adult, or senior."""
    if age < 13:
        print("You are a child.")
    elif 13 <= age < 20:
        print("You are a teenager.")
    elif 20 <= age < 65:
        print("You are an adult.")
    else:
        print("You are a senior.")




def check_grade(grade):
    """Return a message based on the grade."""
    if grade >= 90:
        print("You got an A!")
    elif grade >= 80:
        print("You got a B.")
    elif grade >= 70:
        print("You got a C.")
    elif grade >= 60:
        print("You got a D.")
    else:
        print("You failed.")




def is_even_or_odd(number):
    """Check if a number is even or odd."""
    if number % 2 == 0:
        print(f"{number} is even.")
    else:
        print(f"{number} is odd.")




# Examples of calling the functions
check_age(25)        # Output: You are an adult.
check_grade(85)      # Output: You got a B.
is_even_or_odd(7)    # Output: 7 is odd.






# Additional conditionals
current_date = datetime.now()

# Extract the day of the week
day_of_week = current_date.strftime("%A")
print(day_of_week)

if day_of_week in ["Saturday", "Sunday"]:
    print("It's the weekend!")
else:
    print("It's a weekday.")



temperature = 30
if temperature > 30:
    print("It's hot outside.")
elif temperature < 15:
    print("It's cold outside.")
else:
    print("The weather is nice.")






