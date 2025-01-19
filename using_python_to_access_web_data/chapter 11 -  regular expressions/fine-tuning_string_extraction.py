import re
x = 'From stephen.marquard@uct.ac.za Sat Jan   5 09:14:!6 2008'
y = re.findall('\S+@\S+', x)
print(y)

#\S is non-blank character
# \S+ more than one non-blank character
#\S+@ more than one non-blank character followed by @
#\S+@\S more than one non-blank character followed by @ followed by more than one non-blank character

y = re.findall('^From (\S+@\S+)', x)
print(y)

# Stract after "From "

y = re.findall('\S?+@\S+', x)
print(y)
