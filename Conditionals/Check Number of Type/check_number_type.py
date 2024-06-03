def check_number_type(num):
    if num == 0:
        print("Number is 0")
    elif num < 0:
        print(f"{num} is negative")
    else:
        print(f"{num} is positive")


if __name__ == "__main__":
    number = int(input("Enter a number: "))
    check_number_type(number)
