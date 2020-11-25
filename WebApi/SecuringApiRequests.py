import  urllib.request,urllib.parse,urllib.error
from WebApi.twurl import augment
import json

url = 'https://api.twitter.com/1.1/friends/list.json'

while True:

    print('')
    acct  = input('Ingrese la cuenta de twitter')
    if (len(acct)<1): break

    twitter_url = augment(url,
                        {'screen_name':acct,'count':'5'})

    print('recibiendo',twitter_url)
    connection = urllib.request.urlopen(twitter_url)
    data = connection.read().decode()
    headers = dict(connection.headers)
    print('Remaining',headers['x-rate-limit-remaining'])
    js = json.loads(data)


    for u in js['users']:
        print(u['screen_name'])
        s = u['status']['text']
        print(' ', s[:50])
