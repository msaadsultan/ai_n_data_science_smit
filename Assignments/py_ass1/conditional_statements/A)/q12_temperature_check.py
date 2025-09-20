# 12. Write a program that takes a temperature in Celsius and checks if it’s freezing, moderate, or hot.

temp = float(input("Temperature (°C): "))
if temp <= 0:
    print("Freezing")
elif temp < 30:
    print("Moderate")
else:
    print("Hot")
