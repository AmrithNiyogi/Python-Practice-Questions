# Define the function to compute the Collatz Conjecture sequence for a given number
def collatz_conjecture(num):
    # Continue looping until the number becomes 1
    while num != 1:
        # Print the current number followed by a space, without a newline
        print(num, end=" ")
        # Check if the number is even
        if num % 2 == 0:
            # If even, divide the number by 2
            num = num // 2
        else:
            # If odd, multiply the number by 3 and add 1
            num = (3 * num) + 1
    # Print the final number 1, which ends the sequence
    print(num)

# Ensure the code runs only if this script is executed directly
if __name__ == "__main__":
    # Start an infinite loop to repeatedly ask for user input
    while True:
        # Prompt the user to enter a number and convert it to an integer
        number = int(input("Enter a number: "))
        # Check if the entered number is positive
        if number > 0:
            # If the number is positive, print a message indicating the start of the Collatz sequence
            print("Collatz Conjecture starting from", number)
            # Call the collatz_conjecture function with the entered number
            collatz_conjecture(number)
            # Exit the loop since a valid positive number was entered
            break
        else:
            # If the number is not positive, prompt the user to enter a positive number
            print("Please enter a positive number.")
