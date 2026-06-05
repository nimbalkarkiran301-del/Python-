n = int(input("Enter the number: "))
sum = 0

while n >= 1:
    if n % 2 == 0:
        sum += n
    n -= 1

print("Sum =", sum)