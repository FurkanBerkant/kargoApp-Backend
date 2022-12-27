from flask import request, Blueprint, jsonify
from model import Ilce
from model.db import db
from serialization import IlceSema
from utility import filtrele

ilceBp = Blueprint("ilce", __name__)


@ilceBp.route('/', methods=['GET'])
def getIlce():
    ilceler = filtrele(Ilce).all()
    sema = IlceSema()
    return sema.dump(ilceler, many=True)


@ilceBp.route('/<int:id>', methods=['GET'])
def getIdIlce(id):
    ilce = db.get_or_404(Ilce, id)
    sema = IlceSema()
    return sema.dump(ilce)


@ilceBp.route('/', methods=['POST'])
def postIlce():
    ilceBilgileri = request.json
    ilce = Ilce(**ilceBilgileri)
    db.session.add(ilce)
    db.session.commit()
    sema = IlceSema()
    return sema.dump(ilce)


@ilceBp.route('/<int:id>', methods=['PUT'])
def updateIlce(id):
    ilce = filtrele(Ilce).filter(Ilce.id == id).one_or_none()
    yeniIlceBilgisi = request.json

    sema = IlceSema()
    yeniIlce = sema.load(yeniIlceBilgisi, instance=ilce,
                         session=db.session)
    db.session.commit()

    return sema.dump(yeniIlce)


@ilceBp.route('/<int:id>', methods=['DELETE'])
def deleteIlce(id):
    ilce = db.get_or_404(Ilce, id)
    db.session.delete(ilce)
    db.session.commit()
    return jsonify({'sonuc': 'TAMAM'})
