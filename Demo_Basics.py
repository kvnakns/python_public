
# Variables
player_name = "LeBron James"
player_height = 6.9  # height in feet
player_team = "Los Angeles Lakers"
player_points = 27.0  # average points per game

print(f"Player Name: {player_name}")
print(f"Height: {player_height} feet")
print(f"Team: {player_team}")
print(f"Average Points per Game: {player_points}")


# Loops
print ("\nLoop Practice")

# For loop to print player stats for 5 games
print("Player Stats for 5 Games:")
for game in range(1, 6):
    points_scored = player_points * game  # just a simple multiplication for demo
    print(f"Game {game}: {points_scored} points")


# While loop to count down to the next game
print("\nCountdown to Next Game:")
countdown = 5
while countdown > 0:
    print(f"Game starts in: {countdown} days")
    countdown -= 1




# Conditional statements - allow you to execute code based on certain conditions.

# Conditional statements to check player performance
if player_points > 25:
    print("\nPlayer is having an excellent season!")
elif 20 <= player_points <= 25:
    print("\nPlayer is having a good season!")
else:
    print("\nPlayer needs to improve their performance.")




# Data Types
# Different data types
player_age = 35  # integer
player_average_points = 27.0  # float
player_name = "LeBron James"  # string
player_teams = ["Cleveland Cavaliers", "Miami Heat", "Los Angeles Lakers"]  # list

print(f"Player Age: {player_age}")
print(f"Player Average Points: {player_average_points}")
print(f"Player Name: {player_name}")
print(f"Teams Played For: {player_teams}")




# Functions:  allow you to group code into reusable blocks.

# Function to display player information
def display_player_info(name, height, team, points):
    print(f"Player Name: {name}")
    print(f"Height: {height} feet")
    print(f"Team: {team}")
    print(f"Average Points per Game: {points}")

# Call the function
display_player_info(player_name, player_height, player_team, player_points)

