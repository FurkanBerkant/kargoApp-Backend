from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from .db import db


class Adres(db.Model):
    __tablename__ = 'adresler'

    id = Column(Integer, primary_key=True)
    adres_turu = Column(String)
    adres = Column(String)
    ilId = Column(Integer, ForeignKey('il.id'))
    ilceId = Column(Integer, ForeignKey('ilceler.id'))



    gondericiBilgileri = relationship("GondericiBilgileri", backref="adresler")
    aliciBilgileri = relationship("AliciBilgileri", backref="adresler")
    subeBilgileri = relationship("SubeBilgileri", backref="adresler")
