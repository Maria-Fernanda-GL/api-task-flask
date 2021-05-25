from flask import request, jsonify
from flask import Blueprint

from app.models.model_user import UserModel, UserSchema, db

user_bp = Blueprint('users', __name__)
user_schema = UserSchema()
users_schema = UserSchema(many=True)


@user_bp.route('/api/v1/users', methods=['POST'])
def create_user():
    data = request.json
    email = data['email']
    password = data['password']
    photo = data['photo']

    new_user = UserModel(email=email, password=password, photo=photo)

    db.session.add(new_user)
    db.session.commit()
    return user_schema.jsonify(new_user)


@user_bp.route('/api/v1/users', methods=['GET'])
def get_users():
    users = UserModel.query.all()
    result = users_schema.dump(users)
    return jsonify(result)


@user_bp.route('/api/v1/users/<id>', methods=['GET'])
def get_user(id):
    user = UserModel.query.get(id)
    return user_schema.jsonify(user)


@user_bp.route('/api/v1/users/<id>', methods=['PUT'])
def update_user(id):
    user = UserModel.query.get(id)

    user.title = request.json['title']
    user.description = request.json['description']
    user.start_date = request.json['start_date']
    user.due_date = request.json['due_date']
    user.priority = request.json['priority']

    db.session.commit()
    return user_schema.jsonify(user)


@user_bp.route('/api/v1/users/<id>', methods=['DELETE'])
def delete_user(id):
    user = UserModel.query.get(id)
    db.session.delete(user)
    db.session.commit()
    return user_schema.jsonify(user)
