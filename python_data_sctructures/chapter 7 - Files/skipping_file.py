handle = open('file.txt')
for cheese in handle:
    cheese = cheese.rstrip()
    if not cheese.startswith('Ol'):
        continue
    print(cheese)