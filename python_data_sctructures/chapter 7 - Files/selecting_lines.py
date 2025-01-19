handle = open('file.txt')
for cheese in handle:
    cheese = cheese.rstrip()
    if not 'Ol' in cheese:
        continue
    print(cheese)