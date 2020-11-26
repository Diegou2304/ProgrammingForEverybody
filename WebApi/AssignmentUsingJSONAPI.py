import urllib.parse, urllib.request, urllib.error
import json


url = "http://py4e-data.dr-chuck.net/json?"
key = 42

while True:
    address = input('Enter location here:')
    params = dict()
    params['address'] = address
    params['key'] = key
    final_url = url + urllib.parse.urlencode(params)
    print(final_url)

    temp = urllib.request.urlopen(final_url)
    temp2 = temp.read().decode()
    json = json.loads(temp2)
    print(json['results'][0]['place_id'])

