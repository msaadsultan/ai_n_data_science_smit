# 15. Write a program to check if a number is within a specified range.

n = float(input("Enter number: "))
low = float(input("Range start: "))
high = float(input("Range end: "))
print("Within range" if low <= n <= high else "Out of range")
