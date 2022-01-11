


#http://py4e-data.dr-chuck.net/known_by_Malikye.html  ## You can try this page
from bs4 import BeautifulSoup
import urllib.request,urllib.parse,urllib.error
import re

def URL(url,position,repeat):
    if(repeat is 0):
        return url
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html,'html.parser')
    
    tags = soup('a')
    name = tags[position-1].get('href',None)
    
    finalUrl = URL(name,position,repeat-1)
    return finalUrl
    
    
      

url = input('Enter(url)-')
finalUrl = URL(url,position=18,repeat=7)
#http://py4e-data.dr-chuck.net/known_by_Etinosa.html

#finalUrl gives a string similar to the above one from that string I have to 
# extract the name part

finalName = re.findall('^http://.*_by_([a-zA-Z]+).[a-z]',finalUrl)

print(finalName[0])



