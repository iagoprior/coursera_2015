d = {'a' : 10,'c' : 22, 'b' : 1}
print(sorted(d.items()))

t = sorted(d.items())

for k,v in t:
    print(k,v)