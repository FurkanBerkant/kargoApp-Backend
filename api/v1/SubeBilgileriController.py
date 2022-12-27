from flask import request, Blueprint, jsonify

from model import SubeBilgileri
from model.db import db
from serialization import SubeBilgileriSema
from utility import filtrele

subeBilgileriBp = Blueprint("subeBilgileri", __name__)


@subeBilgileriBp.route('/', methods=['GET'])
def getSubeBilgileri():
    subeBilgileri = filtrele(SubeBilgileri).all()
    sema = SubeBilgileriSema()
    return sema.dump(subeBilgileri, many=True)


@subeBilgileriBp.route('/<int:id>', methods=['GET'])
def getIdSubeBilgileri(id):
    subeBilgileri = db.get_or_404(SubeBilgileri, id)
    sema = SubeBilgileriSema()
    return sema.dump(subeBilgileri)


@subeBilgileriBp.route('/', methods=['POST'])
def postSubeBilgileri():
    subeBilgileri = request.json
    sube = SubeBilgileri(**subeBilgileri)
    db.session.add(sube)
    db.session.commit()

    sema = SubeBilgileriSema()
    return sema.dump(sube)


@subeBilgileriBp.route('/<int:id>', methods=['PUT'])
def updateSubeBilgileri(id):
    subeBilgileri = filtrele(SubeBilgileri).filter(SubeBilgileri.id == id).one_or_none()
    yeniSubeBilgileri = request.json

    sema = SubeBilgileriSema()
    yeniSubeBilgileri = sema.load(yeniSubeBilgileri, instance=subeBilgileri,
                                  session=db.session)
    db.session.commit()

    return sema.dump(yeniSubeBilgileri)


@subeBilgileriBp.route('/<int:id>', methods=['DELETE'])
def deleteSubeBilgileri(id):
    subeBilgileri = db.get_or_404(SubeBilgileri, id)
    db.session.delete(subeBilgileri)
    db.session.commit()
    return jsonify({'sonuc': 'TAMAM'})
