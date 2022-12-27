from flask import request, Blueprint, jsonify
from model import AliciBilgileri
from model.db import db
from serialization import AliciBilgileriSema
from utility import filtrele

aliciBilgileriBp = Blueprint("aliciBilgileri", __name__)


@aliciBilgileriBp.route('/', methods=['GET'])
def getAliciBilgileri():
    aliciBilgileri = filtrele(AliciBilgileri).all()
    sema = AliciBilgileriSema()
    return sema.dump(aliciBilgileri, many=True)


@aliciBilgileriBp.route('/<int:id>', methods=['GET'])
def getIdAliciBilgileri(id):
    aliciBilgileri = db.get_or_404(AliciBilgileri, id)
    sema = AliciBilgileriSema()
    return sema.dump(aliciBilgileri)


@aliciBilgileriBp.route('/', methods=['POST'])
def postAliciBilgileri():
    aliciBilgileri = request.json
    alici = AliciBilgileri(**aliciBilgileri)
    db.session.add(alici)
    db.session.commit()

    sema = AliciBilgileriSema()
    return sema.dump(alici)


@aliciBilgileriBp.route('/<int:id>', methods=['PUT'])
def updateAliciBilgileri(id):
    aliciBilgileri = filtrele(AliciBilgileri).filter(AliciBilgileri.id == id).one_or_none()
    yeniAliciBilgileri = request.json

    sema = AliciBilgileriSema()
    yeniAliciBilgileri = sema.load(yeniAliciBilgileri, instance=aliciBilgileri,
                            session=db.session)
    db.session.commit()

    return sema.dump(yeniAliciBilgileri)


@aliciBilgileriBp.route('/<int:id>', methods=['DELETE'])
def deleteAliciBilgileri(id):
    musteri = db.get_or_404(AliciBilgileri, id)
    db.session.delete(musteri)
    db.session.commit()
    return jsonify({'sonuc': 'TAMAM'})
