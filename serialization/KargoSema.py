from .ma import ma
from model import Kargo


class KargoSema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Kargo
        load_instance = True
