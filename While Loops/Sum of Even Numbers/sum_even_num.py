def sum_of_even_numbers(n):
    total_sum = 0
    current_number = 2  

    while current_number <= n:
        total_sum += current_number
        current_number += 2  

    return total_sum


if __name__ == "__main__":
    num = int(input("Enter a positive integer n: "))
    if num < 1:
        print("Please enter a positive integer.")
    else:
        sum_even = sum_of_even_numbers(num)
        print(f"The sum of all even numbers between 1 and {num} is {sum_even}.")
