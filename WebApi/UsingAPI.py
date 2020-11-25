import urllib.request, urllib.parse, urllib.error
import json


#Need Api Key
serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'

while True:

    address = input('Enter location:')
    if len(address) <1: break

    url = serviceurl + urllib.parse.urlencode({'address':address})

    print('Recibiendo',url)
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    print('Recibido',len(data),'characters')


    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('=====Falla en recibir informacion')
        print(data)
        continue

