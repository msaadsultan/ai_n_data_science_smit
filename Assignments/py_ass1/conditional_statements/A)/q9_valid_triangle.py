# 9. Take three sides of a triangle as input and check if they form a valid triangle.

a = float(input("Side A: "))
b = float(input("Side B: "))
c = float(input("Side C: "))
if a + b > c and a + c > b and b + c > a:
    print("Valid triangle")
else:
    print("Not a triangle")
