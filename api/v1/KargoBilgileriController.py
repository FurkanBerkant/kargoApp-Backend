from flask import request, Blueprint, jsonify

from model import KargoBilgileri
from model.db import db
from serialization import KargoBilgileriSema
from utility import filtrele

kargoBilgileriBp = Blueprint("kargoBilgileri", __name__)


@kargoBilgileriBp.route('/', methods=['GET'])
def getKargoBilgileri():
    kargoBilgileri = filtrele(KargoBilgileri).all()
    sema = KargoBilgileriSema()
    return sema.dump(kargoBilgileri, many=True)


@kargoBilgileriBp.route('/<int:id>', methods=['GET'])
def getIdKargoBilgileri(id):
    kargoBilgileri = db.get_or_404(KargoBilgileri, id)
    sema = KargoBilgileriSema()
    return sema.dump(kargoBilgileri)


@kargoBilgileriBp.route('/', methods=['POST'])
def postKargoBilgileri():
    kargoBilgileri = request.json
    kargo = KargoBilgileri(**kargoBilgileri)
    db.session.add(kargo)
    db.session.commit()

    sema = KargoBilgileriSema()
    return sema.dump(kargo)


@kargoBilgileriBp.route('/<int:id>', methods=['PUT'])
def updateKargoBilgileri(id):
    kargoBilgileri = filtrele(KargoBilgileri).filter(KargoBilgileri.id == id).one_or_none()
    yeniKargoBilgileri = request.json

    sema = KargoBilgileriSema()
    yeniKargoBilgileri = sema.load(yeniKargoBilgileri, instance=kargoBilgileri,
                                       session=db.session)
    db.session.commit()

    return sema.dump(yeniKargoBilgileri)


@kargoBilgileriBp.route('/<int:id>', methods=['DELETE'])
def deleteKargoBilgileri(id):
    kargoBilgileri = db.get_or_404(KargoBilgileri, id)
    db.session.delete(kargoBilgileri)
    db.session.commit()
    return jsonify({'sonuc': 'TAMAM'})
