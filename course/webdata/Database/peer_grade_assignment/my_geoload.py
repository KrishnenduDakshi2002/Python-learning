


from itertools import count
import requests
import sqlalchemy as db
from sqlalchemy import Table,Column,Text
import time

## Dealing the database section

## creating a database to store the raw json file downloaded using the api
engine = db.create_engine('sqlite:///GeoLoad.db')
conn = engine.connect()
metadata = db.MetaData()

Data = Table('Data',metadata,
Column('address_given',Text()),
Column('geoData',Text())
)
Data.drop(engine,checkfirst=True)
Data.create(engine,checkfirst=True)


## Dealing the web section
serviceurl = "http://py4e-data.dr-chuck.net/json?"
api_key = 42
fhandle = open('where.data')
address =''
count =0
for line in fhandle:
    address = line.strip()
    params = {
        'address': address,
        'key': api_key
    }

    response_data = requests.get(serviceurl,params=params)
    print("Receiving....",response_data.url)
    print("Received : ",len(response_data.text)," characters")
    ## I can use .json() -> python dict{} ( this will convert all " " to ' ', so I can't convert that into a dict
    # using json.loads())
    ## .text -> text  but here " " remains same so in future I can convert it into a python dict{}
    query = db.insert(Data).values(address_given = address,geoData= response_data.text)
    res = conn.execute(query)
    
    count = count +1
    if count%10 ==0:
        time.sleep(3)
        print("Pausing for 3 sec ...")

