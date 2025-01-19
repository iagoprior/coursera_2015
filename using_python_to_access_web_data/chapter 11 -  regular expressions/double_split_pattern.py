import re
x = 'From stephen.marquard@uct.ac.za Sat Jan   5 09:14:!6 2008'
y = re.findall('@([^ ]*)', x)
print(y)

#[^ ] is match non-blank character
# * is match many of them