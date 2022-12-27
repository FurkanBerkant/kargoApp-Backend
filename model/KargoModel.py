from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from .db import db


class Kargo(db.Model):
    __tablename__ = 'kargo'
    id = Column(Integer, primary_key=True)
    kargoAdi = Column(String)
    adet = Column(Integer)
    yukseklik = Column(Integer)
    genislik = Column(Integer)
    kirilma = Column(String)
    kargoBilgileri = relationship("KargoBilgileri", backref="kargo")
