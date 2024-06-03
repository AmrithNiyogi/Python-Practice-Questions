def find_largest(a, b, c, d):
    if a >= b:
        if a >= c:
            if a >= d:
                largest = a
            else:
                largest = d
        elif c >= d:
            largest = c
        else:
            largest = d
    elif b >= c:
        if b >= d:
            largest = b
        else:
            largest = d
    elif c >= d:
        largest = c
    else:
        largest = d

    print(f"The largest number is: {largest}")


if __name__ == '__main__':
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    num3 = float(input("Enter the third number: "))
    num4 = float(input("Enter the fourth number: "))
    find_largest(num1, num2, num3, num4)
