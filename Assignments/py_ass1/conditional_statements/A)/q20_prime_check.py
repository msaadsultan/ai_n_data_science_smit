# 20. Create a program that evaluates if an inputted number is prime.

n = int(input("Enter number: "))
if n < 2:
    print("Not prime")
else:
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            print("Not prime")
            break
    else:
        print("Prime")
