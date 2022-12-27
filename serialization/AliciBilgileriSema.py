from . import AdresSema
from .ma import ma
from model import AliciBilgileri
from marshmallow_sqlalchemy import auto_field


class AliciBilgileriSema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = AliciBilgileri
        load_instance = True
        include_fk = True
