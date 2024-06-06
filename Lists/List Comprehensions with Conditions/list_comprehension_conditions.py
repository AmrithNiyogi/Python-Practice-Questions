if __name__ == '__main__':
    odd_numbers = [x for x in range(1, 21) if x % 2 != 0]
    print(f"List of odd numbers in the range 1 to 20: {odd_numbers}\n")

    nums = [-5, 3, -1, 101, -10, 22]
    print(f"List currently: {nums}")
    non_negative_nums = [x for x in nums if x >= 0]
    print(f"List after removing negative numbers: {non_negative_nums}")
