import math as m


def volume_sphere(r):
    return (4/3) * m.pi * r**3


if __name__ == '__main__':
    radius = int(input("Enter the radius of the sphere: "))
    volume = volume_sphere(radius)
    print(f"Volume of sphere with radius {radius}: {volume}")
