# 16. Take the length of three sides and classify the triangle (equilateral, isosceles, or scalene).

a = float(input("Side A: "))
b = float(input("Side B: "))
c = float(input("Side C: "))
if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print("Equilateral")
    elif a == b or b == c or a == c:
        print("Isosceles")
    else:
        print("Scalene")
else:
    print("Not a triangle")
