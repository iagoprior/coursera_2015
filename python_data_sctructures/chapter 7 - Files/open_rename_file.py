#open file
handle = open('file.txt', 'r')
print(handle)
#read a file
handle = open('file.txt')
for cheese in handle:
    print(cheese)
