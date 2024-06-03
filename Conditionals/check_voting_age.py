def check_age(num):
    if num >= 18:
        print("Eligible to vote")
    else:
        print("Not Eligible to vote")


if __name__ == '__main__':
    age = int(input("Enter your age: "))
    check_age(age)
    