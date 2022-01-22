import sqlite3 as sq3

conn = sq3.connect('assignment.db')
conn.execute("INSERT INTO company(id,name,email,salary) VALUES ('#123','Krishnendu Dakshi','kdakshi2018@gmail.com','112000')")





for row in conn.execute("select * from company"):
    print(row[0],row[1],row[2],row[3])

# conn.commit()

print('succesful connection')