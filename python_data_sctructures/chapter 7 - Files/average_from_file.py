# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
count = 0
s = 0
fh = open(fname)
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    if line.startswith("X-DSPAM-Confidence:"):
        count = count + 1
        atpos  = line.find('0')
        sppos = line.find(' ', atpos)
        host = line[atpos : sppos]
        fhost = float(host)
        s = s + fhost

print("Average spam confidence:", s/count )