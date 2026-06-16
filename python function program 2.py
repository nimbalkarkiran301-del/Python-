#write a python program in which function accept list having even number of elements and swap the elements at adjecent position.

def swap_adj(l):
    for i in range(0,len(l),2):
        l[i],l[i+1] = l[i+1],l[i]
    print(l)
        

lst = [10,20,30,40,50,60]
if len(lst) %2 == 0:
    swap_adj(lst)
else:
    print("enter even number of values")
    