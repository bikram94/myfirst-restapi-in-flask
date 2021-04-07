import sqlite3
from flask_restful import Resource, reqparse
from models.user import UserModel


class UserRegister(Resource):

    parser = reqparse.RequestParser()

    parser.add_argument('username',
        type=str,
        required=True,
        help="This filed cannot be left blank"
    )

    parser.add_argument('password',
        type=str,
        required=True,
        help="This filed cannot be left blank"
    )

    def post(self):
        data = UserRegister.parser.parse_args()

        if UserModel.find_by_username(data['username']):
            return {"message": "username already exists"}, 400

        data = UserRegister.parser.parse_args()
        item = UserModel(**data)

        try:
            item.save_to_db()
        except:
            return {'message': 'an error occurred inserting item'}, 500

        return {"message": "User created successfully"}, 201
