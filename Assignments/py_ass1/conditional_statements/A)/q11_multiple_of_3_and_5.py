# 11. Check if a given number is a multiple of both 3 and 5.

n = int(input("Enter number: "))
print("Multiple of both 3 and 5" if n % 3 == 0 and n % 5 == 0 else "No")
