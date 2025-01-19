#print elements of a list

for i in [5,4,3,2,1]:
    print(i)

#list length
x = [1,2,'joe',4]
print(len(x))

#range function
print(range(4))

friends = ['João', 'Maria', 'José', 'Adolf']
print(len(friends))
print(list(range(len(friends))))

#iteration
friends = ['João', 'Maria', 'José', 'Adolf']
for i in friends:
    print('Happy New Year', i)

for i in range(len(friends)):
    friend = friends[i]
    print('Happy New Year', friend)


x = list(range(5))
print(x)