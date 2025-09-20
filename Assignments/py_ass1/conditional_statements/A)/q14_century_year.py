# 14. Check if a year input by the user is a century year.

year = int(input("Enter year: "))
print("Century year" if year % 100 == 0 else "Not a century year")
