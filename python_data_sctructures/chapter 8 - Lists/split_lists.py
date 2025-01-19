abc = 'Hello how are you?'
stuff = abc.split()
print(stuff)
print(len(stuff))
print(stuff[0], stuff[3])

for w in stuff:
    print(w)


line = 'A lot of sugar'
etc = line.split()
print(etc)

line2 = 'first;second;third'
etc2 = line2.split(';')
print(etc2)