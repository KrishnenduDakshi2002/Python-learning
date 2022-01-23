import sqlite3
import re

conn  = sqlite3.connect('CountEmailId.sqlite')
curr = conn.cursor()

curr.execute('Drop table if exists Counts')
curr.execute("create table Counts(org TEXT NOT NULL PRIMARY KEY, count INTEGER)")

fname = input("Enter file name-")
fhandle = open(fname)
for line in fhandle:
    if not line.startswith("From: "):continue
    pieces = line.split()
    EmailId = pieces[1]
    domainName = re.findall('.*@(.*)',EmailId)[0]
    curr.execute('SELECT count FROM Counts WHERE org = ?',(domainName,))
    row = curr.fetchone()

    if row is None:
        curr.execute("INSERT INTO Counts(org,count) VALUES ( ? , 1)",(domainName,))
    else:
        curr.execute("UPDATE Counts SET count = count+1 WHERE org = ?",(domainName,))

    conn.commit()

sum =0
for row in conn.execute("select * from Counts"):
    print(row[0],row[1])
    

