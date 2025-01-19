import urllib.parse, urllib.request, urllib.error
from bs4 import BeautifulSoup
import ssl

#Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#enter: http://py4e-data.dr-chuck.net/comments_42.html
url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('span')
count = 0
sum = 0
for tag in tags:
   # Look at the parts of a tag
   #print('TAG:',tag)
   #print('URL:',tag.get('href', None))
   #print('Contents:',tag.contents[0])
   #print('Attrs:',tag.attrs)
   number = int(tag.contents[0])
   #print(number)
   count = count + 1
   print('Count: ', count)
   sum = sum + number
   print('Sum: ', sum)


