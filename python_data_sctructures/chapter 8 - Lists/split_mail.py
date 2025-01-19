fh = open('mail.txt')
for line in fh:
    line = line.rstrip()
    if not line.startswith("From "):
        continue
    words = line.split()
    print(words[1])


email = words[1]
pieces = email.split('@')
print(pieces)