# Import the random module with an alias 'r' to generate random numbers
import random as r

# Define a function to select a random number between 1 and 100
def select_number():
    # Use randint from the random module to generate a random integer between 1 and 100
    num = r.randint(1, 100)
    # Return the randomly generated number
    return num

# Define a function to check if the guessed number matches the actual number
def guess(guess_number, actual_num):
    # Return True if the guessed number matches the actual number, otherwise False
    return guess_number == actual_num

# Ensure the code runs only if this script is executed directly
if __name__ == "__main__":
    # Initialize a variable to control the loop
    loop_break = False
    # Select a random number to be guessed by the user
    actual_number = select_number()
    
    # Continue looping until the user guesses the correct number
    while not loop_break:
        # Prompt the user to guess a number between 1 and 100 and convert it to an integer
        guessed_number = int(input("Guess a number from 1 to 100: "))
        # Check if the guessed number is correct
        loop_break = guess(guessed_number, actual_number)
        
        # If the guess is correct, print a congratulatory message
        if loop_break:
            print("Congrats! The guess is correct.")
        # If the guessed number is higher than the actual number, inform the user
        elif guessed_number > actual_number:
            print("Guess is high")
        # If the guessed number is lower than the actual number, inform the user
        else:
            print("Guess is low")
