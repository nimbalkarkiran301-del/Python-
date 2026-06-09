#print
#A 
#B C
#D E F
#G H I J
count = ord("A")
for i in range(1, 5):
    for j in range(1 ,i + 1):
        print(chr(count), end=" ")
        count+=1
    print()