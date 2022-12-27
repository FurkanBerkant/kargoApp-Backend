from .ma import ma
from model import SubeBilgileri
from marshmallow_sqlalchemy import auto_field


class SubeBilgileriSema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = SubeBilgileri
        load_instance = True
        include_fk = True
