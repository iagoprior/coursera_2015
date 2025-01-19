data = 'From stephen.marqduc@uct.ac.za Sat Jan 5 09:14:56 2008'

atpos  = data.find('@')
print(atpos)

sppos = data.find(' ', atpos)
print(sppos)

host = data[atpos+1 : sppos]
print(host)