
def divide_numbers():
    attempts = 1  # Allow one retry
    successful = False  # Flag to indicate if the operation was successful


    while attempts <= 2:  # Total of 2 attempts
        try:
            # Prompt user for input
            numerator = float(input("Enter the numerator: "))
            denominator = float(input("Enter the denominator: "))
            
            # Perform division
            result = numerator / denominator
            
            if attempts > 2:
                print("Max attempts reached. Exiting the program.")

        except ZeroDivisionError:
            print("Error: Cannot divide by zero. Please enter a non-zero denominator.")
            attempts += 1  # Increment the attempt counter
            if attempts <= 2:
                print("Let's try again.")
        except ValueError:
            print("Error: Invalid input. Please enter numerical values.")
            attempts += 1  # Increment the attempt counter
            if attempts <= 2:
                print("Let's try again.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            attempts += 1  # Increment the attempt counter
            if attempts <= 2:
                print("Let's try again.")
        else:
            print(f"The result of {numerator} divided by {denominator} is: {result}")
            successful = True  # Mark the operation as successful
            break  # Exit loop if successful

    if not successful:
        print("Max attempts reached. Exiting the program.")







# Call the function
divide_numbers()


