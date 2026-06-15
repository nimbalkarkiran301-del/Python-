#find the same word which number of time present in given sentence.

s = "python is very easy python is programming language"
j = s.split()   # split sentence into words
d = {}

for i in j:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

print(d)
