# Define a function to sum the first n natural numbers
def sum_numbers(n):
    # Initialize the variable to store the sum
    sum = 0
    # Loop to add all numbers from n down to 0
    while n >= 0:
        # Add the current number to the sum
        sum += n
        # Decrement the number by 1
        n -= 1
    # Return the sum of the numbers
    return sum

# Ensure the code runs only if this script is executed directly
if __name__ == "__main__":
    # Prompt the user to enter a number and convert it to an integer
    number = int(input("Enter a number: "))
    # Call the sum_numbers function with the entered number and store the result
    result = sum_numbers(number)
    # Print the result, which is the sum of the first 'number' natural numbers
    print(f"The sum of first {number} natural numbers: {result}")
