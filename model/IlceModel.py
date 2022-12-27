from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from .db import db


class Ilce(db.Model):
    __tablename__ = 'ilceler'
    id = Column(Integer, primary_key=True)
    ilceadi = Column(String)
    adres = relationship("Adres", backref="ilceler")
    sehirid = Column(Integer, ForeignKey('il.id'))
