import sqlite3

conn = sqlite3.connect('spiderwebs.db')
cur = conn.cursor()

# Find the ids that send out page rank - we only are interested
# in pages in the SCC that have in and out links
to_ids = list()
links = list()
cur.execute('''SELECT DISTINCT from_id, to_id FROM Links''')
count = 0
for row in cur:
    from_id = row[0]
    to_id = row[1]
    print(row[0],row[1])
    count = count+1
    if count==40: break
    # if from_id == to_id : continue
    # if from_id not in from_ids : continue
    # if to_id not in from_ids : continue
    # links.append(row)
    # if to_id not in to_ids : to_ids.append(to_id)

# import sqlalchemy as db
# from sqlalchemy import Table,Column,inspect
# from sqlalchemy.orm import Session


# engine = db.create_engine("sqlite:///spiderwebs.db")
# conn = engine.connect()
# metadata = db.MetaData()

# ins = inspect(engine)
# print(ins.get_table_names()) # this will show all tables

# links = Table('links',metadata,autoload=True,autoload_with=engine)

# query = db.select(db.distinct(links.columns.from_id))
# res = Session(bind=engine).execute(query)

# rows = res.fetchall()

# for row in rows:
#     print(row[0],row[1])
    
    

    


