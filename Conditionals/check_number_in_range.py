def is_within_range(number, start, end):
    if start <= number <= end:
        print(f"The number {number} is within the range {start} to {end}.")
    else:
        print(f"The number {number} is not within the range {start} to {end}.")


if __name__ == '__main__':
    num = float(input("Enter the number to check: "))
    range_start = float(input("Enter the start of the range: "))
    range_end = float(input("Enter the end of the range: "))

    is_within_range(num, range_start, range_end)
