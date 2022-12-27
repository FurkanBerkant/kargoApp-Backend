from flask import request, Blueprint, jsonify

from model import  Kargo
from model.db import db
from serialization import KargoSema
from utility import filtrele

kargoBp = Blueprint("kargo", __name__)


@kargoBp.route('/', methods=['GET'])
def getKargo():
    kargo = filtrele(Kargo).all()
    sema = KargoSema()
    return sema.dump(kargo, many=True)


@kargoBp.route('/<int:id>', methods=['GET'])
def getIdKargoBilgileri(id):
    kargo = db.get_or_404(Kargo, id)
    sema = KargoSema()
    return sema.dump(kargo)


@kargoBp.route('/', methods=['POST'])
def postKargo():
    kargo = request.json
    kargo = Kargo(**kargo)
    db.session.add(kargo)
    db.session.commit()

    sema = KargoSema()
    return sema.dump(kargo)


@kargoBp.route('/<int:id>', methods=['PUT'])
def updateKargo(id):
    kargo = filtrele(Kargo).filter(Kargo.id == id).one_or_none()
    yeniKargo = request.json

    sema = KargoSema()
    yeniKargo = sema.load(yeniKargo, instance=kargo,
                                       session=db.session)
    db.session.commit()

    return sema.dump(yeniKargo)


@kargoBp.route('/<int:id>', methods=['DELETE'])
def deleteKargo(id):
    kargo = db.get_or_404(Kargo, id)
    db.session.delete(kargo)
    db.session.commit()
    return jsonify({'sonuc': 'TAMAM'})
