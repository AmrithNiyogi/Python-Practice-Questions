def print_message_n_times(mess, n):
    count = 0

    while count < n:
        print(mess)
        count += 1


if __name__ == "__main__":
    message = input("Enter a message: ")
    num = int(input("Enter the number of times to print the message: "))

    if num > 0:
        print_message_n_times(message, num)
    else:
        print("Please enter a positive integer for the number of times.")
