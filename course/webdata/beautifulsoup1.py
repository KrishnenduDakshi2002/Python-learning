

# http://data.pr4e.org

from bs4 import BeautifulSoup
import urllib.request,urllib.parse,urllib.error


url = input('Enter(url)-')
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html,'html.parser')


# tags[1] -> gives the string at postion 1

tags = soup('a')
for tag in tags:
    print(tag.get('href',None))
