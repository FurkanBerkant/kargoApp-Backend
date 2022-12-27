from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from .db import db


class SubeBilgileri(db.Model):
    __tablename__ = 'subeBilgileri'

    id = Column(Integer, primary_key=True)
    ad = Column(String)
    adres_id = Column(Integer, ForeignKey('adresler.id'))
    telNo = Column(String(11))
    sube_yetkilisi = Column(String)
    kargoBilgileri = relationship("KargoBilgileri", backref="subeBilgileri")
