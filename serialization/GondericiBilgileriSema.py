from .ma import ma
from model import GondericiBilgileri
from marshmallow_sqlalchemy import auto_field


class GondericiBilgileriSema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = GondericiBilgileri
        load_instance = True
        include_fk = True

    adres_id = auto_field()