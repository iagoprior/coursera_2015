y = 0
count = 0
while True:
    sval = input('Enter a number: ')
    if sval == 'done':
        break
    try:
        fval = float(sval)
    except:
        print('Invalid value')
        continue

    y = y + 1
    count = count + fval

print('Average is:', count/y)