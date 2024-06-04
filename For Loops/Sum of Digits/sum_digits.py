def sum_of_digits(num):
    number_str = str(num)
    total_sum = 0
    for digit in number_str:
        total_sum += int(digit)

    return total_sum


if __name__ == '__main__':
    number = int(input("Enter a number: "))
    result = sum_of_digits(number)
    print(f"The sum of the digits of {number} is {result}")
