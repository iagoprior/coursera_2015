import re
x = 'My 2 favorite numbers are 19 and 42'
y = re.findall('[0-9]+',x)
print(y)

y = re.findall('[0-2]+',x)
print(y)

# + is more than 1 digits
y = re.findall('[0-9]',x)
print(y)

y = re.findall('[AEIOU]+',x)
print(y)

y = re.findall('[aeiou]+',x)
print(y)