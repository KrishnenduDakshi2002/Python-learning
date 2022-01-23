
import xml.etree.ElementTree as ET
import sqlite3

conn = sqlite3.connect('Assignment_week3.db')
curr = conn.cursor()

curr.executescript('''
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Genre;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Track;


CREATE TABLE Artist (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Genre (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Album (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id  INTEGER,
    title   TEXT UNIQUE
);

CREATE TABLE Track (
    id  INTEGER NOT NULL PRIMARY KEY 
        AUTOINCREMENT UNIQUE,
    title TEXT  UNIQUE,
    album_id  INTEGER,
    genre_id  INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
)
''')
# for tag and text checking function
def lookup(key_element,text):
    found = False
    for child in key_element:
        if found : return child.text
        if child.tag == 'key' and child.text == text:
            found = True
    return None

fname = input("Enter file name-")
tree = ET.parse(fname)


dict_elements = tree.findall('dict/dict/dict')
# name = lookup(dict_elements[0],'Name')

name = dict_elements[0][3].text
print(name)

# for key_element in dict_elements:
#     if ( lookup(key_element, 'Track ID') is None ) : continue
#     name = lookup(key_element, 'Name')
# #     artist = lookup(key_element, 'Artist')
# #     album = lookup(key_element, 'Album')
# #     count = lookup(key_element, 'Play Count')
# #     rating = lookup(key_element, 'Rating')
# #     length = lookup(key_element, 'Total Time')
#     print(name)

