import math


def is_perfect_square(number):
    if number < 0:
        return False
    sqrt_number = math.isqrt(number)
    return sqrt_number * sqrt_number == number


if __name__ == '__main__':
    num = int(input("Enter a number to check: "))

    if is_perfect_square(num):
        print(f"The number {num} is a perfect square.")
    else:
        print(f"The number {num} is not a perfect square.")
