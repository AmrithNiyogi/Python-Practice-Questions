def check_number(num):
    if num == 0:
        print("Number is 0")
    elif num % 2 == 0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd")


if __name__ == "__main__":
    number = int(input("Enter a number: "))
    check_number(number)
