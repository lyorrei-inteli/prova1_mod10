from flask import Blueprint, jsonify, request

from database.database import db
from database.models import Pedido

api_blueprint = Blueprint("pedido_api", __name__)

@api_blueprint.route("/pedidos", methods=["GET"])
def get_pedidos():
    pedidos = Pedido.query.all()
    return_pedidos = []
    for pedido in pedidos:
        return_pedidos.append(pedido.serialize())
    return jsonify(return_pedidos[::-1])


@api_blueprint.route("/pedidos/<int:id>", methods=["GET"])
def get_pedido(id):
    pedido = Pedido.query.get(id)

    if pedido is None:
        return jsonify({"message": "Pedido não encontrado"}), 500

    return jsonify(pedido.serialize())


@api_blueprint.route("/novo", methods=["POST"])
def create_pedido():
    data = request.json
    pedido = Pedido(user_name=data["user_name"], user_email=data["user_email"], description=data["description"])
    db.session.add(pedido)
    db.session.commit()
    return jsonify(pedido.serialize())


@api_blueprint.route("/pedidos/<int:id>", methods=["PUT"])
def update_pedido(id):
    data = request.json
    pedido = Pedido.query.get(id)

    if pedido is None:
        return jsonify({"message": "Pedido não encontrado"}), 500

    if 'user_name' in data:
        pedido.user_name = data['user_name']
    if 'user_email' in data:
        pedido.user_email = data['user_email']
    if 'description' in data:
        pedido.description = data['description']
    
    db.session.commit()
    return jsonify(pedido.serialize())


@api_blueprint.route("/pedidos/<int:id>", methods=["DELETE"])
def delete_pedido(id):
    pedido = Pedido.query.get(id)

    if pedido is None:
        return jsonify({"message": "Pedido não encontrado"}), 500

    db.session.delete(pedido)
    db.session.commit()
    return jsonify(pedido.serialize())