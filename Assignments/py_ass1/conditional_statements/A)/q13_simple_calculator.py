# 13. Take two numbers and an operator (+, -, *, /) as input and perform the corresponding operation.

a = float(input("First number: "))
b = float(input("Second number: "))
op = input("Operator (+, -, x, /): ")
if op == "+":
    print(a + b)
elif op == "-":
    print(a - b)
elif op.lower() == "x":
    print(a * b)
elif op == "/":
    print("Infinity" if b == 0 else a / b)
else:
    print("Invalid operator")
