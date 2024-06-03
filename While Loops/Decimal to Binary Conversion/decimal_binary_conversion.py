def decimal_to_binary(dec_number):
    if dec_number == 0:
        return "0"

    binary_rep = ""

    while dec_number > 0:
        remainder = dec_number % 2
        binary_rep = str(remainder) + binary_rep
        dec_number = dec_number // 2

    return binary_rep


if __name__ == "__main__":
    decimal_number = int(input("Enter a decimal number: "))
    binary_representation = decimal_to_binary(decimal_number)
    print(f"The binary representation of {decimal_number} is {binary_representation}.")
