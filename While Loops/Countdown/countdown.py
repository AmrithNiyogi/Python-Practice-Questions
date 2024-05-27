# Import the time module to use the sleep function
import time

# Define a function to perform a countdown from a given number of seconds
def countdown(secs):
    # Continue looping while the number of seconds is greater than 0
    while secs > 0:
        # Print the current time left in seconds
        print(f"Time left is: {secs} seconds")
        # Pause execution for 1 second
        time.sleep(1)
        # Decrement the number of seconds by 1
        secs -= 1
    
    # Print a message indicating the countdown has ended
    print("Countdown has ended")

# Ensure the code runs only if this script is executed directly
if __name__ == "__main__":
    # Prompt the user to enter the number of seconds for the countdown and convert it to an integer
    seconds = int(input("Enter the number of seconds: "))
    # Call the countdown function with the entered number of seconds
    countdown(seconds)
