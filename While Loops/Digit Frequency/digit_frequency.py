def count_digit_frequency(number):
    digit_frequency = {'0': 0, '1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0}
    num_str = str(number)
    index = 0
    while index < len(num_str):
        digit_frequency[num_str[index]] += 1
        index += 1

    return digit_frequency


if __name__ == '__main__':
    num = input("Enter a number: ")

    if num.startswith('-'):
        num = num[1:]

    frequency = count_digit_frequency(num)

    print("Digit frequency:")
    for digit, count in frequency.items():
        if count > 0:
            print(f"{digit}: {count}")
