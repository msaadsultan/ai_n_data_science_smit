# 2. Take a user’s age as input and display whether they are a minor, adult, or senior citizen.

age = int(input("Enter age: "))
if age < 18:
    print("Minor")
elif age < 60:
    print("Adult")
else:
    print("Senior Citizen")
