import logging

from data import config
from gino import Gino
from sqlalchemy import Column, Integer, String, BigInteger, sql

db = Gino()

class User(db.Model):
    id = Column(Integer, primary_key=True)
    user_id = Column(BigInteger, unique=True)
    first_name = Column(String(55))
    query: sql.Select
class Projects(db.Model):
    id = Column(Integer, primary_key=True)
    project_name = Column(String(55), unique=True)
    project_description = Column(String(255))
    project_link = Column(String(255))
    project_photo = Column(String(255))
    query: sql.Select

async def create_db():
    await db.set_bind(config.db_uri, )
    logging.info(config.db_uri)
    await db.gino.drop_all()
    await db.gino.create_all()
