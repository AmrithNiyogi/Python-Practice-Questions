def product_numbers(num1, num2):
    return num1 * num2


if __name__ == '__main__':
    number1 = int(input("Enter the first number:"))
    number2 = int(input("Enter the second number:"))
    result = product_numbers(number1, number2)
    print(f"Product of {number1} * {number2}: {result}")
