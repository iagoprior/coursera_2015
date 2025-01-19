x = -1
print('Before', x)

for numbers in [1,2,3,4,5,6,7,8,9,10,11,12]:
    if numbers > x:
        x = numbers

print('The largest number is: ', x)