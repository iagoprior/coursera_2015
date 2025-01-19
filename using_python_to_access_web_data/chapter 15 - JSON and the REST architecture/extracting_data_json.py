import json
import urllib.request
import xml.etree.ElementTree as ET

url = input('Enter location: ')
if len(url) < 1 :
    url = 'http://py4e-data.dr-chuck.net/comments_2145959.json'
#url2: http://py4e-data.dr-chuck.net/comments_2145959.json
#url: http://py4e-data.dr-chuck.net/comments_42.json

print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read()
print('Retrieved',len(data),'characters')
info = json.loads(data)
#print(info)
counts = len(info['comments'])
#print(counts)
sum = 0
for i in info['comments']:
    # Debug print the data :)
    #print(i['count'])
    sum = sum + i['count']

print('Count:', counts)
print('Sum:', sum)

#count = info['comments'][2]['count']
#print(count)