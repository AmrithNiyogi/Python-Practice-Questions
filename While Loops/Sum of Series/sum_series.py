def sum_of_series(n):
    if n <= 0:
        return "Please enter a positive integer."

    total_sum = 0.0
    i = 1

    while i <= n:
        total_sum += 1 / i
        i += 1

    return total_sum


if __name__ == "__main__":
    n = int(input("Enter a positive integer n: "))
    result = sum_of_series(n)
    if isinstance(result, str):
        print(result)
    else:
        print(f"The sum of the series 1 + 1/2 + 1/3 + ... + 1/{n} is {result:.4f}.")
