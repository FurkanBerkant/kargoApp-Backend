from .ma import ma
from model import Ilce
from marshmallow_sqlalchemy import auto_field


class IlceSema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Ilce
        load_instance=True
        include_fk = True
