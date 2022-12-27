from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from .db import db


class Il(db.Model):
    __tablename__ = 'il'
    id = Column(Integer, primary_key=True)
    ilAdi = Column(String)
    adres = relationship("Adres", backref="il")
    ilce = relationship("Ilce", backref="il")
