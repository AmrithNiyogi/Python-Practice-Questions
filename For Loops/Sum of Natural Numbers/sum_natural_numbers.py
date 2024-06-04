def sum_numbers(n):
    sum_num = 0
    for i in range(1, n + 1):
        sum_num += i
    return sum_num


if __name__ == '__main__':
    num = int(input("Enter a number: "))
    sum_number = sum_numbers(num)
    print(f"The sum of numbers from 1 to {num}: {sum_number}")
