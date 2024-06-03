def classify_triangle(s1, s2, s3):
    if s1 == s2 == s3:
        print("Triangle is Equilateral")
    elif (s1 == s2) or (s2 == s3) or (s1 == s3):
        print("Triangle is Isosceles")
    else:
        print("Triangle is Scalene")


if __name__ == '__main__':
    side1 = int(input("Enter side 1 of triangle: "))
    side2 = int(input("Enter side 2 of triangle: "))
    side3 = int(input("Enter side 3 of triangle: "))
    classify_triangle(side1, side2, side3)
