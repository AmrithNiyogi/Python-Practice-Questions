def largest_number(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        return num1
    elif num2 > num1 and num2 > num3:
        return num2
    else:
        return num3


if __name__ == '__main__':
    number1 = int(input("Enter the first number: "))
    number2 = int(input("Enter the second number: "))
    number3 = int(input("Enter the third number: "))
    largest = largest_number(number1, number2, number3)
    print(f"The largest of {number1}, {number2} and {number3}: {largest}")
