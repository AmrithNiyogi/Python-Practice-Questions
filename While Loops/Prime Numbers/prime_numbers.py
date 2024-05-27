# Define a function to check if a given number is a prime number
def check_prime(n):
    # Check if the number is less than or equal to 1
    if n <= 1:
        # Numbers less than or equal to 1 are not prime
        return False
    # Check if the number is exactly 2
    elif n == 2:
        # 2 is a prime number
        return True
    # Check if the number is even
    elif n % 2 == 0:
        # Even numbers greater than 2 are not prime
        return False
    
    # Initialize a variable to check odd factors starting from 3
    i = 3
    # Loop through potential factors from 3 to n-1
    while i < n:
        # Check if the current factor divides n without a remainder
        if n % i == 0:
            # If a factor is found, n is not a prime number
            return False
        # Increment the factor by 2 to check the next odd number
        i += 2
    
    # If no factors are found, n is a prime number
    return True

# Ensure the code runs only if this script is executed directly
if __name__ == "__main__":
    # Prompt the user to enter an integer and convert it to an integer
    number = int(input("Enter an integer: "))
    # Check if the entered number is a prime number
    if check_prime(number):
        # If the number is prime, print a message indicating it is a prime number
        print(f"{number} is a prime number.")
    else:
        # If the number is not prime, print a message indicating it is not a prime number
        print(f"{number} is not a prime number.")
