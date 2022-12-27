from . import AliciBilgileriSema, GondericiBilgileriSema, KargoSema, SubeBilgileriSema
from .ma import ma
from model import KargoBilgileri
from marshmallow_sqlalchemy import auto_field
class KargoBilgileriSema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = KargoBilgileri
        include_fk = True
        load_instance = True


    kargo= ma.Nested(KargoSema)
    aliciBilgileri = ma.Nested(AliciBilgileriSema)
    gondericiBilgileri = ma.Nested(GondericiBilgileriSema)
    subeBilgileri=ma.Nested(SubeBilgileriSema)
