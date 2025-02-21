astr = 'Hello Bob'
try:
    istr = int(astr)
except:
    istr = print("Encontrei erro, por favor passe número entre 1 e 100")

print('First', istr)

astr = '123'
try:
    istr = int(astr)
except:
    istr = -1

print('Second', istr)