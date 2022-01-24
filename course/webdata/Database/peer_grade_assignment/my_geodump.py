
import sqlalchemy as db
from sqlalchemy import Table,Column,Text, engine,inspect
import json
import codecs


engine = db.create_engine('sqlite:///Geoload.db')
conn = engine.connect()
metadata = db.MetaData()

fhand = codecs.open('where_in_map.js', 'w', "utf-8")
fhand.write("myData = [\n")

Inspector = inspect(engine)
Data = db.Table('Data',metadata,autoload=True,autoload_with=engine)
res = conn.execute(db.select(Data.columns.geoData)).all()

for geodata in res:
    jfile = json.loads(geodata[0])
    lat = jfile['results'][0]['geometry']['location']['lat']
    lng = jfile['results'][0]['geometry']['location']['lng']
    foradd = jfile['results'][0]['formatted_address']
    
    fhand.write(",\n")
    foradd = foradd.replace("'", "")
    output = "["+str(lat)+","+str(lng)+", '"+foradd+"']"
    fhand.write(output)
    
    
    if lat==22.99139:
        print("************ MY ENGINEERING COLLEGE'S ADDRESS ***********")
    print(foradd , lat ,lng)
    print(" ")
    
fhand.write("\n];\n")
fhand.close()
