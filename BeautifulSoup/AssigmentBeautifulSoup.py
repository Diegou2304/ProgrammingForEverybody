import urllib.request, urllib.error,urllib.parse

from bs4 import BeautifulSoup

import ssl



ctx  = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


url = "http://py4e-data.dr-chuck.net/comments_1045582.html"
html = urllib.request.urlopen(url,context = ctx).read()
soup = BeautifulSoup(html,'html.parser')


tags = soup('span')
temp_sum = 0
for tag in tags:

    temp_sum = temp_sum + int(tag.contents[0].encode())


print(temp_sum)