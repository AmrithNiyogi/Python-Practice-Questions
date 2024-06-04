def print_pyramid(n):
    for i in range(1, n + 1):
        print(" " * (n - i), end="")
        print("*" * (2 * i - 1))


if __name__ == "__main__":
    levels = int(input("Enter the number of levels for the pyramid: "))
    print("Pyramid pattern with", levels, "levels:")
    print_pyramid(levels)
