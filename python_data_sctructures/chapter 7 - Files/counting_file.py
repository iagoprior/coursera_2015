handle = open('file.txt')
count = 0
for cheese in handle:
    count = count + 1
print('Line count: ', count)
