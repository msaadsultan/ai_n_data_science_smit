# 8. Create a program that checks if a given string is a palindrome.

s = input("Enter string: ")
print("Palindrome" if s == s[::-1] else "Not palindrome")
