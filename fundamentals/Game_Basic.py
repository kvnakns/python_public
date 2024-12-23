
import random

def game_intro():
    print("")
    print("Welcome to the Number Guessing Game!")
    print("")
    print("I'm thinking of a number between 1 and 100. Can you guess what it is?")
    print("")



def number_guessing_game():
    # Introduction to the game
    game_intro()

    # Variables
    number_to_guess = random.randint(1, 100)
    guess = None
    attempts = 0

    # Loop to allow multiple guesses
    while guess != number_to_guess:
        guess = int(input("Enter your guess: "))
        attempts += 1

        # Conditional Statements
        if guess < number_to_guess:
            print("Too low! Try again.")
        elif guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts.")






# Run the game
number_guessing_game()
