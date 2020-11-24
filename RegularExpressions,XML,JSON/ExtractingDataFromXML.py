import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET


fhand = urllib.request.urlopen('http://py4e-data.dr-chuck.net/comments_1045584.xml').read()

stuff = ET.fromstring(fhand)
lst = stuff.findall('comments/comment')
print("User count:", len(lst))
cuenta = 0
for item in lst:
    cuenta =  cuenta + int(item.find('count').text)

print(cuenta)

