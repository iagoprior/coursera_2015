fname = input('Enter the filename: ')
try:
    fhand = open(fname)
except:
    print('File cannot be oppened: ', fname)
    quit()

count = 0
for line in fhand:
    if line.startswith('Meu') :
        count = count + 1
print('There were', count, 'Meu lines in ', fname)