# 17. Write a program that asks for an integer and checks if it’s divisible by 2, 3, or both.

n = int(input("Enter integer: "))
if n % 2 == 0 and n % 3 == 0:
    print("Divisible by both 2 and 3")
elif n % 2 == 0:
    print("Divisible by 2")
elif n % 3 == 0:
    print("Divisible by 3")
else:
    print("Not divisible by 2 or 3")
