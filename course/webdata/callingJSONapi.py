#enter the following line 
# Moscow Institute of Physics & Technology
import json
import urllib.parse,urllib.error,urllib.request

api_key = 42
serviceUrl = 'http://py4e-data.dr-chuck.net/json?'
    

address = input('Enter address-')
dic={}
dic['address']= address
dic['key']=api_key
url = serviceUrl + urllib.parse.urlencode(dic)

decodedFile = urllib.request.urlopen(url).read().decode()
jsonfile = json.loads(decodedFile)
print(jsonfile['results'][0]['place_id'])


