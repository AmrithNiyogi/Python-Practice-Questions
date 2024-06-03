def divisible(num):
    if num % 3 == 0 and num % 5 == 0:  # can also be written as if num % 15 == 0
        print("Divisible")
    else:
        print("Not Divisible")


if __name__ == '__main__':
    number = int(input("Enter a number to check if divisible by 3 and 5: "))
    divisible(number)
