def square_number(num):
    return num ** 2


if __name__ == '__main__':
    number1 = int(input("Enter a number:"))
    result = square_number(number1)
    print(f"Square of {number1} : {result}")
