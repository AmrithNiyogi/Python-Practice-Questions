if __name__ == '__main__':
    items = ["pen", "pencil", "paper"]
    print(f"List is: {items}")
    index = items.index("pencil")
    items[index] = "eraser"
    print(f"List after changing item: {items}\n")

    values = [2, 4, 6, 8]
    print(f"The list values: {values}")
    new_values = []
    for value in values:
        element = value * 2
        new_values.append(element)

    print(f"The list values after doubling: {new_values}")
  
