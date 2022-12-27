import datetime

from sqlalchemy import Column, Integer, ForeignKey, DateTime, String
from .db import db


class KargoBilgileri(db.Model):
    __tablename__ = 'kargoBilgileri'

    id = Column(Integer, primary_key=True)
    kargoId=Column(Integer, ForeignKey('kargo.id'))
    aliciId = Column(Integer, ForeignKey('aliciBilgileri.id'))
    gondericiId = Column(Integer, ForeignKey('gondericiBilgileri.id'))
    subeId = Column(Integer, ForeignKey('subeBilgileri.id'))
    kargo_tarihi = Column(DateTime,default=datetime.datetime.utcnow())
    kargo_odemeTuru = Column(String)
