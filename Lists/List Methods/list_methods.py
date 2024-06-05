if __name__ == '__main__':
    # creating the list animals
    animals = ["cat", "dog", "rabbit", "elephant"]
    # sorting the list using the inbuilt sort function
    print(f"The list before sorting: {animals}")
    animals.sort()
    print(f"The list after sorting: {animals}")
    # reversing the list using the reverse function
    animals.reverse()
    print(f"The reversed list: {animals}")
    # removing the element 'rabbit' from the list
    animals.remove('rabbit')
    print(f"The list after removal: {animals}")
    
