def sum_of_powers_recursive(digits, num_digits):
    if not digits:
        return 0
    return (int(digits[0]) ** num_digits) + sum_of_powers_recursive(digits[1:], num_digits)


def is_armstrong(number):
    num_str = str(number)
    num_digits = len(num_str)
    sum_of_powers = sum_of_powers_recursive(num_str, num_digits)
    return sum_of_powers == number


if __name__ == '__main__':
    num = int(input("Enter a number to check: "))

    if is_armstrong(num):
        print(f"The number {num} is an Armstrong number.")
    else:
        print(f"The number {num} is not an Armstrong number.")