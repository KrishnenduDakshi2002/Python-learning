
import os
import xml.etree.ElementTree as ET

fileName = 'Testingxml.xml'
fullFilePath = os.path.abspath(os.path.join('webdata',fileName)) #this is the full path of .xml
#file, if we don't add this line we will get error in ET.parse()


# if we store xml as string
# input = '''<account>
#               <gmail>
#                   <name>
#       '''
# like this 
# then we use   stuff = ET.fromstring(input)
stuff = ET.parse(fullFilePath)
lst = stuff.findall('gmail')
for item in lst:
    print('Name gmail account :',item.find('name').text)
    print('Attribute :',item.get("x"))


