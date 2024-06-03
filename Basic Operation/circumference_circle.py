import math as m


def circumference_circle(r):
    return 2 * m.pi * r


if __name__ == '__main__':
    radius = int(input("Enter the radius of the circle: "))
    circumference = circumference_circle(radius)
    print(f"Circumference of circle with radius {radius}: {circumference}")
