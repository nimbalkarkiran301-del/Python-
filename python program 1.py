#WAP to enter numbers till user wants end at the end it should displays sum of all the numbers enters.
sum=0
ch='yes'
while ch=='yes':
    n=int(input("Enter a number:"))
    sum=sum+n
    ch=input ("You want to enter more numbers:")
print ("sum of all numbers:",sum)   