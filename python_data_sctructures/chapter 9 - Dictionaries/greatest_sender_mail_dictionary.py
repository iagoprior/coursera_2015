name = input("Enter file:")
if len(name) < 1:
    name = "mbox.txt"
handle = open(name)

counts = dict()
for line in handle:
    line = line.rstrip()
    if not line.startswith("From "):
        continue
    words = line.split()
    lista = words[1]
    print(lista)
    counts[lista] = counts.get(lista, 0) + 1

print(counts)


bigcount = None
bigword = None
for word, count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

print(bigword, bigcount)
