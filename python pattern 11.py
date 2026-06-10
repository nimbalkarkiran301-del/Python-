#print
#A
#b C
#d E f
#G h I j
n = 4
ch = ord('A')

for i in range(1, n + 1):
    for j in range(1, i + 1):
        if ch % 2 == 0:
            print(chr(ch).lower(), end=" ")
        else:
            print(chr(ch), end=" ")
        ch += 1
    print()