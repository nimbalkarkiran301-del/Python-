num = int(input("Enter the number: "))
org = num
rev = 0

while num > 0:
    rim = num % 10
    rev = (rev * 10) + rim
    num = num // 10

print("Reverse number =", rev)

if org == rev:
    print("Number is palindrome")
else:
    print("Number is not palindrome")