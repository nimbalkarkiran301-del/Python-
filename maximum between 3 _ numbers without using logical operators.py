#wap to find maximum between three numbers without using logical operators
a = int(input ("Enter the first number: "))
b = int(input ("Enter the second number: "))
c = int(input ("Enter the third number: "))
if a>b:
 if a>c:
    print("A is greater")
 else:
    print("C is greater")
else:
 if b>c:
     print("B is grater")
 else:  
     print("C is greater")