from .ma import ma
from model import Il


class IlSema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Il
        load_instance=True