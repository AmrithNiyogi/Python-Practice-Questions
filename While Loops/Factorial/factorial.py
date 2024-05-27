# Define a function to compute the factorial of a given number
def factorial(n):
    # Initialize the factorial result to 1
    fact = 1
    # Continue looping while the value of n is greater than 0
    while n > 0:
        # Multiply the current factorial result by n
        fact *= n
        # Decrement the value of n by 1
        n -= 1
    # Return the computed factorial result
    return fact

# Ensure the code runs only if this script is executed directly
if __name__ == "__main__":
    # Prompt the user to enter a number and convert it to an integer
    number = int(input("Enter a number: "))
    # Call the factorial function with the entered number and store the result
    result = factorial(number)
    # Print the result of the factorial calculation
    print(f"The factorial of {number} is: {result}")
