
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, MetaData, Table, Column,String


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db = SQLAlchemy(app)
meta = MetaData()


students = Table(
    'students',meta,
    Column('User_id',Integer,nullable = False,primary_key = True),
    Column('User_name',String(128),nullable = False),
    Column('phone_num',String(64),nullable = False),
    Column('email_id',String(128),nullable = False)
)

db.create_all()