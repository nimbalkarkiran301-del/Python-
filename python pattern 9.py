#print
#  * * * *
#    * * *
#      * *
#        *
n = 4

for i in range(n):
    for k in range(i):
        print("  ", end="")   # two spaces for indentation
    for j in range(n - i):
        print("*", end=" ")
    print()
