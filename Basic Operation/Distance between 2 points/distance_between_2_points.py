import math as m


def distance_of_two_point(x1, x2, y1, y2):
    return m.sqrt((x2 - x1)**2 + (y2-y1)**2)


if __name__ == '__main__':
    coord_x1 = int(input("Enter the x coordinate of point 1:"))
    coord_y1 = int(input("Enter the y coordinate of point 1:"))
    coord_x2 = int(input("Enter the x coordinate of point 2:"))
    coord_y2 = int(input("Enter the y coordinate of point 2:"))
    distance = distance_of_two_point(coord_x1, coord_x2, coord_y1, coord_y2)
    print(f"Distance between points P1({coord_x1}, {coord_y1}) and P2({coord_x2}, {coord_y2}): {distance}")
