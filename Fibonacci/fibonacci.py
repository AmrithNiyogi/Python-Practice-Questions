# Define a function to generate and print the first n numbers of the Fibonacci series
def fibonacci(n):
    # Initialize the first two numbers of the Fibonacci series
    num_1 = 0
    num_2 = 1
    # Initialize the count with 2 since the first two numbers are already defined
    count = 2
    # Print the first two numbers separated by a space
    print(num_1, num_2, sep=" ", end=" ")
    
    # Continue looping to generate the remaining Fibonacci numbers until count reaches n
    while count < n:
        # Calculate the next number in the series
        num_3 = num_1 + num_2
        # Update num_1 to the next number in the series
        num_1 = num_2
        # Update num_2 to the newly calculated number
        num_2 = num_3
        # Print the current Fibonacci number followed by a space
        print(num_2, sep=" ", end=" ")
        # Increment the count by 1
        count += 1

# Ensure the code runs only if this script is executed directly
if __name__ == "__main__":
    # Prompt the user to enter the number of Fibonacci numbers to generate and convert it to an integer
    number = int(input("Enter a number: "))
    # Print a message indicating the start of the Fibonacci series output
    print(f"Fibonacci Series for the first {number} numbers: ")
    # Call the fibonacci function with the entered number
    fibonacci(number)
