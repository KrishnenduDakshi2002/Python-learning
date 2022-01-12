
## Example of .xml
#http://py4e-data.dr-chuck.net/comments_1427864.xml
#http://py4e-data.dr-chuck.net/comments_42.xml


import xml.etree.ElementTree as ET
import urllib.request,urllib.parse,urllib.error

url = input('Enter filename-')
xmlfile = urllib.request.urlopen(url).read()
data = xmlfile.decode()  ## decoding the byte string to unicode
comntinfo = ET.fromstring(data) ## here data is string
lst = comntinfo.findall('comments/comment') ## this list will store all tree whose root is comment
sum =0
for i in range(0,len(lst),1):
    sum = sum + int(lst[i].find('count').text)

print(sum)



 
