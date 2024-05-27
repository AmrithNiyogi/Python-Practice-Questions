# Define a function to sum the digits of a given number
def sum_digits(n):
    # Initialize the variable to store the sum of digits
    sum = 0
    # Check if the number is negative
    if n < 0:
        # Print a message indicating negative values are not allowed and the absolute value will be used
        print("Negative values are not allowed. Taking the absolute value of the number entered.")
        # Take the absolute value of the number
        n = abs(n)
    
    # Loop to sum the digits of the number
    while n != 0:
        # Extract the last digit of the number
        digit = n % 10
        # Add the digit to the sum
        sum = sum + digit
        # Remove the last digit from the number
        n = n // 10
    
    # Return the sum of the digits
    return sum

# Ensure the code runs only if this script is executed directly
if __name__ == "__main__":
    # Prompt the user to enter a number and convert it to an integer
    number = int(input("Enter a number: "))
    # Print the entered number
    print(f"Entered number: {number}")
    # Call the sum_digits function with the entered number and store the result
    result = sum_digits(number)
    # Print the sum of the digits
    print(f"Sum of digits: {result}")
