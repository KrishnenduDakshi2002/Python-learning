import requests
from bs4 import BeautifulSoup
import ssl
from urllib.request import urlopen

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# url = 'https://docs.python-requests.org/en/latest/user/quickstart/'
url ='http://python-data.dr-chuck.net/'
page = requests.get(url)

# print(page.content.title)
content_type = page.headers['content-type']
# print(content_type.find(';'))
# print(content_type[:9])

print((page.headers['content-type'])[:9])



file = open('html.txt','w')

file.write(page.content.decode())
# print(page.content.decode())

# doc = urlopen(url,context=ctx)
# print(type(doc.read()))


soup = BeautifulSoup(page.content,'html.parser') # page.content is binary 
tags = soup('a')

spurl = ''

for tag in tags:
    if tag.get('href') == 'known_by_42.html':
        spurl = tag.get('href')
        

# if not  spurl.startswith('https://') or spurl.startswith('http://') :
#     spurl = url + spurl
# spurlPg = requests.get(spurl)
# print(spurlPg.content.decode())


        