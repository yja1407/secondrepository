import sqlite3
from flask_restful import Resource,reqparse
from flask import Request
from models.user import UserModel


class UserRegister(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('username',
        type=str,
        required=True,
        help="This field can't be blank"
    )
    parser.add_argument('password',
        type=str,
        required=True,
        help="This field can't be blank"
    )
    def post(self):
        data = UserRegister.parser.parse_args()
        if UserModel.find_by_username(data['username']):
            return {"message":"user already exists"},400

        user=UserModel(data['username'],data['password'])
        user.save_to_userdb()
##        connection  = sqlite3.connect('data.db')
##        cursor = connection.cursor()
##        user_register_query = "INSERT INTO users VALUES (NULL,?,?)"
##        cursor.execute(user_register_query, (data['username'],data['password']))
##        select_query = "SELECT * FROM users"
##        for row in cursor.execute(select_query):
##            print(row)
##        connection.commit()
##        connection.close()
        return {"message":"User was created successfully"}, 201
