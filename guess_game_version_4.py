# TOP Googlers Group 7 Python Guess Number Game Code 
# Version 1.1
# Created on May 9th 2022
# Created by Emmanual, Kaliman & Dhruv
# Inspired by Christopher Sziklas & Nicholas Kelly :) 
# Contact at: dhruvil.thakkar@rackspace.com

# Import random module for randint function
import random

# Greet the player.
player_name = input("Enter your name: ")
print("Welcome to the guessing number game", player_name)

# Function to check if users input is a valid integer
def check_int_number(user_input):
    while True:
        try:
            user_input = int(user_input)
            if user_input <= 0:
                user_input=input("Not a valid input. Please enter a value greate then 0: ")
                continue
            return user_input
        except ValueError:
            user_input = input("Not an integer!. Please enter valid input: ")


# Ask for max range and validate through check_int_number function
user_max_range = input("Enter a max range: ")
max_range = check_int_number(user_max_range)
print("We will play the numbers between 1 to", max_range)

# Pick a random number between 1 to max_range to play
num = random.randint(1, max_range)

# Initialize guess variable to none
guessing = None

# Count variable for number of attempts
no_of_attempts = 0

# Count variable for number of games

no_of_games_played =0
# Main Game Logic
while guessing != num:
    #print(num) #uncomment this to see the number selected
    guessing = input("Please guess a number: ")
    guessing = check_int_number(guessing)
    no_of_attempts += 1
    if guessing == num: # If guess is correct, congratulate player 
        no_of_games_played += 1
        print("Fantastic! you made correct guess and have won $50 today. Number of attempts for correct guess were:",no_of_attempts)
        again = None  # Loop to validate users input for yes or no
        while again not in ['Yes', 'Y', 'y', 'N', 'n', 'No','YES','no']:
            again = input("Do you want to play again? Enter Yes or No or Y or N: ")
            if again.lower() == 'y' or again.lower() == 'yes':
                user_max_range = input("Enter a max range: ")
                max_range = check_int_number(user_max_range)
                print("We will play the numbers between 1 to", max_range)
                num = random.randint(1, max_range)
                guessing = None
                no_of_attempts = 0
                continue
            elif again.lower() == 'n' or again.lower() == 'no':
                print("Thank you for playing. Have a nice Day!. You played {0} games total today".format(no_of_games_played))
            else:
                continue
    elif guessing > num: # print number is high or low and ask player to guess again
        print("Tuff luck, sorry. Your guess is too high. Please try again! This was attempt number:",no_of_attempts)
    else:
        print("Tuff luck, sorry. Your guess is too low. Please try again! This was attempt number:",no_of_attempts)

