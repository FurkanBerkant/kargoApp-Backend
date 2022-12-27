from flask import request, Blueprint, jsonify
from model import Adres
from model.db import db
from serialization import AdresSema
from utility import filtrele

adresBp = Blueprint("adres", __name__)


@adresBp.route('/', methods=['GET'])
def getAdres():
    adresler = filtrele(Adres).all()
    sema = AdresSema()
    return sema.dump(adresler, many=True)


@adresBp.route('/<int:id>', methods=['GET'])
def getIdAdres(id):
    adres = db.get_or_404(Adres, id)
    sema = AdresSema()
    return sema.dump(adres)


@adresBp.route('/', methods=['POST'])
def postAdres():
    adresBilgileri = request.json
    adres = Adres(**adresBilgileri)
    db.session.add(adres)
    db.session.commit()

    sema = AdresSema()
    return sema.dump(adres)


@adresBp.route('/<int:id>', methods=['PUT'])
def updateAdres(id):
    adres = filtrele(Adres).filter(Adres.id == id).one_or_none()
    yeniAdresBilgisi = request.json

    sema = AdresSema()
    yeniAdres = sema.load(yeniAdresBilgisi, instance=adres,
                          session=db.session)
    db.session.commit()

    return sema.dump(yeniAdres)


@adresBp.route('/<int:id>', methods=['DELETE'])
def deleteAdres(id):
    adres = db.get_or_404(Adres, id)
    db.session.delete(adres)
    db.session.commit()
    return jsonify({'sonuc': 'TAMAM'})
