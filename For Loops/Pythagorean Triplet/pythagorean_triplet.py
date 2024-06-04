def triplet(a, b, c):
    sides = [a, b, c]
    sides.sort()
    return sides[0]**2 + sides[1]**2 == sides[2]**2


if __name__ == '__main__':
    numbers = []
    for i in range(3):
        num = int(input(f"Enter number {i + 1}: "))
        numbers.append(num)

    if triplet(numbers[0], numbers[1], numbers[2]):
        print(f"The numbers {numbers} form a Pythagorean triplet.")
    else:
        print(f"The numbers {numbers} do not form a Pythagorean triplet.")
