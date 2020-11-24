import xml.etree.ElementTree as ET
data = ''' <person>
<name> Diego </name>
<phone type = "intl">
+1 456 888 555
</phone>
</person>
'''

tree = ET.fromstring(data)
print('Name:',tree.find('name').text)

stuff = ET.fromstring(input)
lst = stuff.findall('users/user')
for item in lst:
