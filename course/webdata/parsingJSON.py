

#http://py4e-data.dr-chuck.net/comments_1427865.json
import json
import urllib.parse,urllib.request,urllib.error

url = input('Enter filename-')
jsonfile = urllib.request.urlopen(url).read()
decodedFile = jsonfile.decode()
info = json.loads(decodedFile)
sum =0
dicOflist = info['comments']

for item in range(0,len(dicOflist),1):
    sum =sum +int(dicOflist[item]['count'])
    
print(sum)

