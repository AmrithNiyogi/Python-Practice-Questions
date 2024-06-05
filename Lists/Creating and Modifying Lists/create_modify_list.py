if __name__ == '__main__':
    # creating a list
    my_list = ['New York', 'London', 'Paris']
    print(f"Initial List: {my_list}")
    # adding 'Tokyo' to the end of the list
    # the append() function adds the new element to the end of the list
    my_list.append('Tokyo')
    print(f"List after appending: {my_list}")
    # inserting 'Sydney' at the 2nd position
    # the insert() function is used to add a new element at a specific position
    # indexes for lists start from 0, meaning 2nd position is the 1st index
    my_list.insert(1, 'Sydney')
    print(f"List after insertion: {my_list}")
