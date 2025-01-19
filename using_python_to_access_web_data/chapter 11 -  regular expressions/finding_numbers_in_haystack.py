import  re
hand = open('regex_sum.txt')
numlist = list()
sum = 0
count = 0
for line in hand:
    line = line.rstrip()
    stuff = re.findall('[0-9]+', line)
    numlist = stuff + numlist
print(numlist)

for i in numlist:
    sum = sum + int(i)
    count = count + 1
print(sum)
print(count)

import  re
hand = open('regex_sum_2.txt')
numlist = list()
sum = 0
count = 0
for line in hand:
    line = line.rstrip()
    stuff = re.findall('[0-9]+', line)
    numlist = stuff + numlist
print(numlist)

for i in numlist:
    sum = sum + int(i)
    count = count + 1
print(sum)
print(count)
