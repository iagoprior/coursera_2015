handle = open('file.txt')
for cheese in handle:
    cheese = cheese.rstrip()
    if cheese.startswith('Ol'):
        print(cheese)
    elif cheese.startswith('Meu'):
        print(cheese)
    elif cheese.startswith('Estou'):
        print(cheese)