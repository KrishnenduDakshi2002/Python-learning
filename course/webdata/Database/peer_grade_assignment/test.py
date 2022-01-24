


import requests
import sqlalchemy as db
from sqlalchemy import Table,Column,Text


engine = db.create_engine('sqlite:///Test.db')
conn = engine.connect()
metadata = db.MetaData()

Data = Table('Data',metadata,
Column('address_given',Text()),
Column('geoData',Text())
)
Data.drop(engine,checkfirst=True)
Data.create(engine,checkfirst=True)



address = 'Institute of Business and Modern Technologies'
serviceurl = "http://py4e-data.dr-chuck.net/json?"
api_key = 42
params = {
    'address':address,
    'key': api_key
}

def printList(lst):
    for i in lst:
        print(i)

# print(requests.get(serviceurl,params=params))

#it may return python dict for json object
# it amy return python list for json array

## response_data['results'][0]['geometry']['location'] ## lat and lng # float
## response_data['results'][0]['formatted_address']  ## formatted address # str
response_data = requests.get(serviceurl,params=params)
print(response_data.url)
print(len(response_data.text))
query = db.insert(Data).values(address_given = address,geoData = response_data.text)
res = conn.execute(query)

