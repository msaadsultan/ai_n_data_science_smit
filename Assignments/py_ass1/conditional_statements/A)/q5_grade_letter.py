# 5. Ask the user for a grade percentage and display the corresponding letter grade (A, B, C, D, F).

score = float(input("Enter percentage: "))
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")
