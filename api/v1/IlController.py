from flask import request, Blueprint, jsonify
from model import Il
from model.db import db
from serialization import IlSema
from utility import filtrele

ilBp = Blueprint("il", __name__)


@ilBp.route('/', methods=['GET'])
def getIl():
    iller = filtrele(Il).all()
    sema = IlSema()
    return sema.dump(iller, many=True)


@ilBp.route('/<int:id>', methods=['GET'])
def getIdIl(id):
    il = db.get_or_404(Il, id)
    sema = IlSema()
    return sema.dump(il)


@ilBp.route('/', methods=['POST'])
def postIl():
    ilBilgileri = request.json
    il = Il(**ilBilgileri)
    db.session.add(il)
    db.session.commit()
    sema = IlSema()
    return sema.dump(il)


@ilBp.route('/<int:id>', methods=['PUT'])
def updateIl(id):
    il = filtrele(Il).filter(Il.id == id).one_or_none()
    yeniIlBilgisi = request.json

    sema = IlSema()
    yeniIl = sema.load(yeniIlBilgisi, instance=il,
                       session=db.session)
    db.session.commit()

    return sema.dump(yeniIl)


@ilBp.route('/<int:id>', methods=['DELETE'])
def deleteIl(id):
    il = db.get_or_404(Il, id)
    db.session.delete(il)
    db.session.commit()
    return jsonify({'sonuc': 'TAMAM'})
