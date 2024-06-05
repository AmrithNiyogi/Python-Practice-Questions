if __name__ == '__main__':
    # Creating a list comprehension for squares of numbers from 1 to 15
    # the last value of range is not included, therefore to print till 15, we give the end value as 16
    squares = [x ** 2 for x in range(1, 16)]
    print("List of squares from 1 to 15:", squares)
    # Creating a list comprehension for even numbers between 1 and 20
    # the last value of range is not included, therefore to print till 20, we give the end value as 21
    # x % 2 == 0 is the condition that determines if a number is even, basically it checks if the number divided gives remainder 0
    evens = [x for x in range(1, 21) if x % 2 == 0]
    print("List of even numbers between 1 and 20:", evens)
    
