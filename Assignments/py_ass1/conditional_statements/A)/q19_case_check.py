# 19. Check if a string input is uppercase, lowercase, or a mix.

s = input("Enter string: ")
if s.isupper():
    print("Uppercase")
elif s.islower():
    print("Lowercase")
else:
    print("Mixed")
