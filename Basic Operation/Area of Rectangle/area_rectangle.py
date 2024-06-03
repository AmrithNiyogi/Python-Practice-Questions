def area_rectangle(ln, br):
    return ln * br


if __name__ == '__main__':
    length = int(input("Enter the length of the rectangle: "))
    breadth = int(input("Enter the breadth of the rectangle: "))
    area = area_rectangle(length, breadth)
    print(f"Area of rectangle with sides {length} and {breadth}: {area}")
    
