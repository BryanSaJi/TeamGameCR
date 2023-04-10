from flask import Blueprint, request, jsonify
from TeamGameCR.Models.User import User
from main import db


bp = Blueprint('user', __name__)

@bp.route('/users', methods=['GET'])
def listar_users():
    users = User.query.all()
    resultado = []
    for user in users:
        resultado.append({'id': user.id, 'name': user.nombre, 'email': user.email})
    return jsonify({'users': resultado})

@bp.route('/users/<int:id>', methods=['GET'])
def obtener_user(id):
    user = User.query.get(id)
    if user:
        return jsonify({'id': user.id, 'name': user.nombre, 'email': user.email})
    else:
        return jsonify({'Msg': 'User not found'}), 404

@bp.route('/users', methods=['POST'])
def crear_user():
    name = request.json['name']
    email = request.json['email']
    user = User(name=name, email=email)
    db.session.add(user)
    db.session.commit()
    return jsonify({'Msg': 'A new user was created succesfully'})

@bp.route('/users/<int:id>', methods=['PUT'])
def actualizar_user(id):
    user = User.query.get(id)
    if user:
        name = request.json['name']
        email = request.json['email']
        user.name = name
        user.email = email
        db.session.commit()
        return jsonify({'Msg': 'User updated succesfully'})
    else:
        return jsonify({'Msg': 'User not found'}), 404

@bp.route('/users/<int:id>', methods=['DELETE'])
def eliminar_user(id):
    user = User.query.get(id)
    if user:
        db.session.delete(user)
        db.session.commit()
        return jsonify({'Msg': 'User deleted succesfully'})
    else:
        return jsonify({'Msg': 'User not found'}), 404