# Check if all elements in a tuple are same or not

t = (10, 20, 30, 40, 50)

s = set(t)
print(s)

if len(s) == 1:
    print("same")
else:
    print("not same")