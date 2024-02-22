from flask import request, jsonify
from . import app, db
from .models import User
from .enums import Gender


@app.route('/user', methods=['GET'])
def get_users():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    users_query = User.query.paginate(page=page, per_page=per_page, error_out=False)
    users = users_query.items

    return jsonify({
        'users': [user.to_dict() for user in users],
        'total': users_query.total,
        'pages': users_query.pages,
        'current_page': page
    })


@app.route('/user', methods=['POST'])
def add_user():
    data = request.get_json()
    try:
        user = User(
            name=data['name'],
            gender=Gender(data['gender'])
        )
        db.session.add(user)
        db.session.commit()
        return jsonify(user.to_dict()), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400


@app.route('/user/<int:uid>', methods=['PUT'])
def edit_user(uid):
    user = User.query.get(uid)
    if not user:
        return jsonify({'error': 'User not found'}), 404

    data = request.get_json()
    name = data.get('name')
    gender = data.get('gender')

    if name:
        user.name = name
    if gender:
        try:
            user.gender = Gender[gender.upper()]
        except KeyError:
            return jsonify({'error': 'Invalid gender'}), 400

    db.session.commit()
    return jsonify(user.to_dict())
