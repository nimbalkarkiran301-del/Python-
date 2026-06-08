num = int(input("Enter the number: "))
org = num
sum = 0

while num > 0:
    rim = num % 10
    sum = sum + rim ** 3
    num = num // 10

if org == sum:
    print("Number is Armstrong")
else:
    print("Number is not Armstrong")
    