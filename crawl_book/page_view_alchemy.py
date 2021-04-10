import re
from string import ascii_uppercase

from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from crawl_book.requestsbs4 import RequestBs

AUTHOR_RULE = '">(.*)</h1>'
BRIEF_RULE = '''<p>(.*)</p>'''

engine = create_engine("mysql+pymysql://root:admin@localhost/phone?charset=UTF8")
Base = declarative_base()

class PageView(Base):
    __tablename__ = 'django_pageview'

    id = Column(Integer, primary_key=True)
    read = Column(Integer)
    comments = Column(Integer)
    book_id = Column(Integer)

    def __init__(self, read, comments, book_id):
        self.read = read
        self.comments = comments
        self.book_id = book_id

Base.metadata.create_all(engine)

dbsession = sessionmaker(bind=engine)
session = dbsession()

for i in range(1, 143):
    add = PageView(read=0, comments=0, book_id=i)
    session.add(add)
    session.commit()
    session.close()
