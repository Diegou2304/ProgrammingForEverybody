import urllib.request, urllib.parse, urllib.error
import json

serviceurl = 'http://maps.googleapis.com/maps/pi/geocode/json?'

while True:

    address = input('Enter location:')
    if len(address) <1: break

    url = serviceurl + urllib.parse.urlencode({'address':address})
    