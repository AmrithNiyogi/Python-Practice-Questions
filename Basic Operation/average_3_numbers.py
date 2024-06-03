def average(num1, num2, num3):
    return (num1 + num2 + num3) / 3


if __name__ == '__main__':
    number1 = int(input("Enter the first number:"))
    number2 = int(input("Enter the second number:"))
    number3 = int(input("Enter the third number:"))
    avg = average(number1, number2, number3)
    print(f"Average of {number1}, {number2}, {number3}: {avg}")
