import urllib.request, urllib.parse
import json, ssl
# Ann Arbor, MI
#Butantã, SP
#Barão Geraldo, Campinas
# Heavily rate limited proxy of https://www.geoapify.com/ api
serviceurl = 'https://py4e-data.dr-chuck.net/opengeo?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    address = address.strip()
    parms = dict()
    parms['q'] = address

    url = serviceurl + urllib.parse.urlencode(parms)

    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'features' not in js:
        print('==== Download error ===')
        print(data)
        break

    if len(js['features']) == 0:
        print('==== Object not found ====')
        print(data)
        break


    lat = js['features'][0]['properties']['lat']
    lon = js['features'][0]['properties']['lon']
    a = js['features'][0]
    #print(a)
    #print('lat', lat, 'lon', lon)
    location = js['features'][0]['properties']['formatted']
    #print(location)
    display = js['features'][0]['properties']['timezone']['display_name']
    #print(display)
    code = js['features'][0]['properties']['plus_code']
    print('Plus code', code)
    #print(json.dumps(js, indent=4))




