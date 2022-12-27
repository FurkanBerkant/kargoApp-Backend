from . import IlSema, IlceSema
from .ma import ma
from model import Adres
from marshmallow_sqlalchemy import auto_field


class AdresSema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Adres
        load_instance = True
        include_fk = True

    il = ma.Nested(IlSema)
    ilceler = ma.Nested(IlceSema)

