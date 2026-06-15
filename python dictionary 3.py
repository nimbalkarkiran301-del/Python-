#create dictionary in another way.and perform simple operations.
d1 = dict(one=1, two=2)
print(d1)
print(d1.keys())
print(d1.values())
print(d1.items())
print(d1.get('a'))
d1.popitem()         # removes last item
print(d1)
d1['a']="two"
print(d1)
d1['a'] = "one"
print(d1)
d1.clear()
print(d1)