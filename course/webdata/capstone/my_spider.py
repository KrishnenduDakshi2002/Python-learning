
# http://python-data.dr-chuck.net

#
import sqlalchemy as db
from sqlalchemy import Table, Column, UniqueConstraint, engine, inspect, Integer, Text, REAL, insert, select, delete, update
from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import func
from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin, urlparse


# creating tables

engine = db.create_engine("sqlite:///spiderwebs.db")
conn = engine.connect()
metadata = db.MetaData()

pages = Table('pages', metadata,
Column('id', Integer(), primary_key=True, autoincrement=True),
Column('url', Text, unique=True),
Column('html', Text),
Column('error', Integer()),
Column('old_rank', REAL),
Column('new_rank', REAL)
)

links = Table('links', metadata,
Column('from_id', Integer()),
Column('to_id', Integer()),
UniqueConstraint('from_id', 'to_id')
)

webs = Table('webs', metadata,
Column('web', Text, unique=True))

metadata.create_all(engine)

# Database modeling completed


# checking for any progress

# if we did  any progress then we will not start from the base url
query = select(pages.columns.url).order_by(func.random()).limit(1)
res = Session(bind=engine).execute(query)

if res.fetchone() is not None:
       print("Continuing crawling from the existing database .... ")
else:
       starturl = input("Enter starting url - ")
       if (starturl.endswith('.htm') or starturl.endswith('.html')):
              pos = starturl.rfind('/')
              starturl = starturl[:pos]
       r1 = conn.execute(insert(webs).values(web=starturl))  # inserted into webs
       r2 = conn.execute(insert(pages).values(url=starturl, new_rank=1.0))


# getting the currnet web

res = Session(bind=engine).execute(select(webs))

web = list()
for i in res:
       web.append(str(i[0]))
print(web)

# OK

many = 0
while True:
       if many < 1:
              sval = input("How many pages - ")
              many = int(sval)
              if many < 1: break
      
       many = many - 1

       session = Session(bind=engine)

       try:  # pages.columns.html == None
              res = session.execute(select(pages).order_by(func.random()).limit(1).where(pages.columns.error == None, pages.columns.html == None))
              items = res.fetchall()[0]
              url = items[1]
              fromid = items[0]
       except:
              print('No unretrieved HTML pages found')
              many = 0
              break

       print(fromid, url, end=" ")

       # deleting
       
       r = conn.execute(db.delete(links,links.columns.from_id == fromid))

       # now it's time for getting the page for these url
       try:
              document = requests.get(url)
              document_in_unicode = document.content.decode()

              if document.status_code != 200:
                     print("Error in page : ", document.status_code)
                     r = conn.execute(update(pages).where(pages.columns.url == url).values(error=document.status_code, url=url))

              if (document.headers['content-type'])[:9] != 'text/html':
                     print("Ignoring non text/html pages")
                     r = conn.execute(db.delete(pages,pages.columns.url == url))
                     continue

              print('('+str(len(document_in_unicode))+')', end=' ')
              # example {fromId , url , total words in html} =>>>  1 http://python-data.dr-chuck.net (1475)

              # time for parsing the html file for href
              # document.content  => byte type
              soup = BeautifulSoup(document.content, 'html.parser')

       except KeyboardInterrupt:
              print('')
              print('[WARNING]:Program interrupted by user...')
              break

       except:
              print("[ERROR]:unable to parse the page ")
              r = session.execute(update(pages).where(
                  pages.columns.url == url).values(error=-1))

       try:  # if that url is present then will skip
              r = conn.execute(insert(pages).values(url=url))
       except:
              None

       try:
              r = conn.execute(db.update(pages, pages.columns.url == url, {'html': document_in_unicode}))

       except:
              print("[ERROR]: updating html in database")

       # retrieving all anchor tags
       tags = soup('a')
       count = 0
       for tag in tags:
              href = tag.get('href', None)
              if (href is None): continue
              up = urlparse(href)
              if (len(up.scheme) < 1):
                     href = urljoin(url, href)
              ipos = href.find('#')
              if (ipos > 1): href = href[:ipos]
              if ( href.endswith('.png') or href.endswith('.jpg') or href.endswith('.gif') ) : continue
              if ( href.endswith('/') ) : href = href[:-1]
              if (len(href)<1): continue
              # Check if the URL is in any of the webs
              found = False
              for row in web:
                     if ( href.startswith(row) ) :
                            found = True
                            break
              if not found : continue
              
              try:
                     r = conn.execute(insert(pages).values(url=href,new_rank = 1.0))
              except:
                     None
                     
              count = count+1
                     
              try:
                     r = Session(bind=engine).execute(select(pages.columns.id).limit(1).where(pages.columns.url == href))
                     
                     ids = r.fetchone()
                     toid = ids[0]
                     # print('Printing to_id',toid)
                     
              except:
                     print('Could not retrieve id')
                     continue
              
              try:
                     r = conn.execute(insert(links).values(from_id = fromid,to_id = toid))
              except:
                     None
                     
       print(count)