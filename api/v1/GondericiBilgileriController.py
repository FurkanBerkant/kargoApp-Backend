from flask import request, Blueprint, jsonify

from model import GondericiBilgileri
from model.db import db
from serialization import GondericiBilgileriSema
from utility import filtrele

gondericiBilgileriBp = Blueprint("gondericiBilgileri", __name__)


@gondericiBilgileriBp.route('/', methods=['GET'])
def getAliciBilgileri():
    gondericiBilgileri = filtrele(GondericiBilgileri).all()
    sema = GondericiBilgileriSema()
    return sema.dump(gondericiBilgileri, many=True)


@gondericiBilgileriBp.route('/<int:id>', methods=['GET'])
def getIdGondericiBilgileri(id):
    gondericiBilgileri = db.get_or_404(GondericiBilgileri, id)
    sema = GondericiBilgileriSema()
    return sema.dump(gondericiBilgileri)


@gondericiBilgileriBp.route('/', methods=['POST'])
def postGondeiciBilgileri():
    gondericiBilgileri = request.json
    gonderi = GondericiBilgileri(**gondericiBilgileri)
    db.session.add(gonderi)
    db.session.commit()

    sema = GondericiBilgileriSema()
    return sema.dump(gonderi)


@gondericiBilgileriBp.route('/<int:id>', methods=['PUT'])
def updateGondericiBilgileri(id):
    gondericiBilgileri = filtrele(GondericiBilgileri).filter(GondericiBilgileri.id == id).one_or_none()
    yeniGondericiBilgileri = request.json

    sema = GondericiBilgileriSema()
    yeniGondericiBilgileri = sema.load(yeniGondericiBilgileri, instance=gondericiBilgileri,
                                       session=db.session)
    db.session.commit()

    return sema.dump(yeniGondericiBilgileri)


@gondericiBilgileriBp.route('/<int:id>', methods=['DELETE'])
def deleteGondericiBilgileri(id):
    gondericiBilgileri = db.get_or_404(GondericiBilgileri, id)
    db.session.delete(gondericiBilgileri)
    db.session.commit()
    return jsonify({'sonuc': 'TAMAM'})
