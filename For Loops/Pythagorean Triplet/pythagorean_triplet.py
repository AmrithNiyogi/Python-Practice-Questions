import math as m


def triplet(a, b, c):
    if (m.pow(a, 2) + m.pow(b, 2) == m.pow(c, 2) or
            m.pow(b, 2) + m.pow(c, 2) == m.pow(a, 2) or
            m.pow(a, 2) + m.pow(c, 2) == m.pow(b, 2)):
        return True
    else:
        return False


if __name__ == '__main__':
    side1 = int(input("Enter the first number: "))
    side2 = int(input("Enter the second number: "))
    side3 = int(input("Enter the third number: "))
    if triplet(side1, side2, side3):
        print(f"{side1}, {side2}, {side3} form a Pythagorean Triplet")
    else:
        print(f"{side1}, {side2}, {side3} do not form a Pythagorean Triplet")
