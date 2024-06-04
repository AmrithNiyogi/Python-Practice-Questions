def print_table(num):
    for i in range(1, 11):
        print(f"{num} * {i} = {num*i}")


if __name__ == '__main__':
    number = int(input("Enter an number to print multiplication tables of: "))
    print_table(number)
    
