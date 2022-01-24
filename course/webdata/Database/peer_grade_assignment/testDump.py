


import requests
import sqlalchemy as db
from sqlalchemy import Table,Column,Text, engine,inspect
import json


engine = db.create_engine('sqlite:///Test.db')
conn = engine.connect()
metadata = db.MetaData()

Inspector = inspect(engine)
print(Inspector.get_table_names())

Data = db.Table('Data',metadata,autoload=True,autoload_with=engine)
query = db.select(Data.columns.geoData).where(Data.columns.address_given =='Institute of Business and Modern Technologies')
res = conn.execute(query).all()

for rows in res:

    jfile = json.loads(rows[0])
    print("lat : ",jfile['results'][0]['geometry']['location']['lat'])
    print("lng : ",jfile['results'][0]['geometry']['location']['lng'])
    print("forward address : ",jfile['results'][0]['formatted_address'])


