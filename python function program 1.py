#write a python function that accept the number and check whether it's perfect number or not.
def perfect(n):
    s = 0
    for i in range(1, n):
        if n % i == 0:
            s = s + i
            
    if s == n:
        print(n, "is a Perfect Number")
    else:
        print(n, "is Not a Perfect Number")

num = int(input("Enter a number: "))
perfect(num)