#write a python program create new tuple which contain elements are multiple of 7 in given number.
t1 = (14, 18, 26, 29, 30)

t2 = ()

for i in t1:
    if i % 7 == 0:
        t2 = t2 + (i,)

print("New tuple:", t2)