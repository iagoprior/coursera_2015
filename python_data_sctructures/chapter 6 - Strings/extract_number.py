text = "X-DSPAM-Confidence:    0.8475"
atpos  = text.find('0')

sppos = text.find('5', atpos)

host = text[atpos : sppos+5]
print(float(host))