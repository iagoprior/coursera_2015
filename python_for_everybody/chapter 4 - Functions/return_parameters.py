def greet(lang):
    if lang == 'es':
        return 'Hola'
    elif lang == 'fr':
        return 'Bonjour'
    else:
        return 'Hello'

print(greet('es'),'Gleen')
print(greet('fr'), 'Sally')
print(greet('br'), 'Julia')
