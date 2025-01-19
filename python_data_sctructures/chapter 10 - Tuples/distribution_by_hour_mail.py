name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

counts = dict()
for line in handle:
    line = line.rstrip()
    if not line.startswith("From "):
        continue
    words = line.split()
    lista = words[5]
    # print(lista)
    hours = lista[:2]
    hours = hours.split()
    # print(hours)

    for word in hours:
        counts[word] = counts.get(word, 0) + 1

# print(counts)

lst = list()
for key, val in counts.items():
    newtup = (key, val)
    lst.append(newtup)

lst = sorted(lst, reverse=False)

for key, val in lst:
    print(key, val)