def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def print_primes_up_to(n):
    for num in range(2, n + 1):
        if is_prime(num):
            print(num, end=' ')


if __name__ == '__main__':
    number = int(input("Enter the upper limit to print prime numbers: "))
    print(f"Prime numbers up to {number} are:")
    print_primes_up_to(number)
