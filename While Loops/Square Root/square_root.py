def babylonian_sqrt(number, tolerance=1e-10):
    if number < 0:
        return "Cannot compute the square root of a negative number"

    if number == 0:
        return 0

    guess = number / 2.0
    while True:
        new_guess = (guess + number / guess) / 2.0
        if abs(new_guess - guess) < tolerance:
            return new_guess
        guess = new_guess


if __name__ == "__main__":
    num = float(input("Enter a number to find the square root: "))
    result = babylonian_sqrt(num)
    print(f"The square root of {num} is approximately {result}")
