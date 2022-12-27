from flask import Blueprint
from .IlController import ilBp
from .IlceController import ilceBp
from .AdresController import adresBp
from .AliciBilgileriController import aliciBilgileriBp
from .GondericiBilgileriController import gondericiBilgileriBp
from .SubeBilgileriController import subeBilgileriBp
from .KargoBilgileriController import kargoBilgileriBp
from .KargoController import kargoBp


apiv1_bp = Blueprint("apiv1", __name__)
apiv1_bp.register_blueprint(ilBp, url_prefix="/il")
apiv1_bp.register_blueprint(ilceBp, url_prefix="/ilce")
apiv1_bp.register_blueprint(adresBp, url_prefix="/adres")
apiv1_bp.register_blueprint(aliciBilgileriBp, url_prefix="/aliciBilgileri")
apiv1_bp.register_blueprint(gondericiBilgileriBp, url_prefix="/gondericiBilgileri")
apiv1_bp.register_blueprint(subeBilgileriBp, url_prefix="/subeBilgileri")
apiv1_bp.register_blueprint(kargoBilgileriBp, url_prefix="/kargoBilgileri")
apiv1_bp.register_blueprint(kargoBp, url_prefix="/kargo")


