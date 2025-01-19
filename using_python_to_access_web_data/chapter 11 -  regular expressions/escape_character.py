import re
x = 'We just received $10.00 for cookies.'
y = re.findall('\$[0-9.]+',x)
print(y)

# starts with dollar, look for digit or period one or more time