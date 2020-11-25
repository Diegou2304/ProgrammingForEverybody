import urllib.request, urllib.parse, urllib.error
import json


url = "http://py4e-data.dr-chuck.net/comments_1045585.json"

#This does not return readable data from url
temp = urllib.request.urlopen(url)
json_temp = temp.read().decode()
json = json.loads(json_temp)

json_length = len(json['comments'])
suma = 0
for x in range(json_length):

    suma = suma + json['comments'][x]['count']


print(suma)