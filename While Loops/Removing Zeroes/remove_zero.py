def remove_zeroes(number):
    res = 0
    multiplier = 1

    while number > 0:
        digit = number % 10
        number //= 10

        if digit != 0:
            res += digit * multiplier
            multiplier *= 10

    return res


if __name__ == "__main__":
    num = int(input("Enter a number: "))
    result = remove_zeroes(num)
    print(f"Number after removing all zeroes: {result}")
