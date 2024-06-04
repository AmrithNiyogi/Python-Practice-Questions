def harmonic_sum(num):
    h_sum = 0.0
    for i in range(1, num + 1):
        h_sum += 1 / i
    return h_sum

if __name__ == '__main__':
    n = int(input("Enter the number of terms (n): "))
    result = harmonic_sum(n)
    print(f"The harmonic sum of the first {n} natural numbers is: {result}")
