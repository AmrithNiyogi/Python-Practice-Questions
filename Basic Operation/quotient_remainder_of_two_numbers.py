def quotient_number(num1, num2):
    return num1 / num2


def remainder_number(num1, num2):
    return num1 % num2


if __name__ == '__main__':
    number1 = int(input("Enter the first number:"))
    number2 = int(input("Enter the second number:"))
    quot = quotient_number(number1, number2)
    rem = remainder_number(number1, number2)
    print(f"Quotient of {number1} / {number2}: {quot}")
    print(f"Remainder of {number1} / {number2}: {rem}")
