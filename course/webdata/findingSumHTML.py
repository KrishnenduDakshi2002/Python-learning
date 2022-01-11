
# example of extracting tags and contents from a HTMl page
#https://www.py4e.com/code3/urllink2.py?PHPSESSID=fc98d4902a52354e1e604b9dac6e407b


from bs4 import BeautifulSoup
import urllib.request,urllib.parse,urllib.error


url = input('Enter(url)-')
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html,'html.parser')

tags = soup('span')
sum =0
for tag in tags:
    sum = sum + int(tag.contents[0]) # tag.contents[0] gives string


print(sum)