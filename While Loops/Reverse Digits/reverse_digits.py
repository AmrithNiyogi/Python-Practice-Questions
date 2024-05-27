# Define a function to reverse the digits of a given number
def reverse(n):
    # Initialize the variable to store the reversed number
    reversed_number = 0
    # Check if the number is negative
    if n < 0:
        # Print a message indicating negative values are not allowed and the absolute value will be used
        print("Negative values are not allowed. Taking the absolute value of the number entered.")
        # Take the absolute value of the number
        n = abs(n)
    
    # Loop to reverse the digits of the number
    while n != 0:
        # Extract the last digit of the number
        digit = n % 10
        # Append the digit to the reversed number
        reversed_number = (reversed_number * 10) + digit
        # Remove the last digit from the number
        n = n // 10
    
    # Return the reversed number
    return reversed_number

# Ensure the code runs only if this script is executed directly
if __name__ == "__main__":
    # Prompt the user to enter a number and convert it to an integer
    number = int(input("Enter a number: "))
    # Print the entered number
    print(f"Entered number: {number}")
    # Call the reverse function with the entered number and store the result
    reversed_num = reverse(number)
    # Print the reversed number
    print(f"Reversed Number: {reversed_num}")
