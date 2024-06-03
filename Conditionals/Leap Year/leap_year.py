def check_leap_year(yr):
    if yr % 4 == 0:
        if yr % 100 == 0:
            if yr % 400 == 0:
                print("Leap year")
            else:
                print("Not a Leap year")
        else:
            print("Leap year")
    else:
        print("Not a Leap year")


if __name__ == '__main__':
    year = int(input("Enter the year to check: "))
    check_leap_year(year)
