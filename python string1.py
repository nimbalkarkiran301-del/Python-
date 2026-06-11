# Write a Python program to count alphabets, digits, special symbols,
# uppercase letters, and lowercase letters.

str1 = "Kiran@123"

A = 0      # Alphabets
D = 0      # Digits
S = 0      # Special Symbols
U = 0      # Uppercase
L = 0      # Lowercase

for i in str1:
    if i.isalpha():
        A += 1

        if i.islower():
            L += 1
        else:
            U += 1

    elif i.isdigit():
        D += 1

    else:
        S += 1
        
print("Alphabets =", A)
print("Digits =", D)
print("Special Symbols =", S)
print("Uppercase Letters =", U)
print("Lowercase Letters =", L)