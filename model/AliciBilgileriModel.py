from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship

from .db import db


class AliciBilgileri(db.Model):
    __tablename__ = 'aliciBilgileri'

    id = Column(Integer, primary_key=True)
    adres_id = Column(Integer, ForeignKey('adresler.id'))
    tcKimlik = Column(String(11))
    ad = Column(String)
    soyad = Column(String)
    telNo = Column(String(11))
    email = Column(String)
    kargoBilgileri = relationship("KargoBilgileri", backref="aliciBilgileri")
