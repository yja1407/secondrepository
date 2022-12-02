import sqlite3
from dbalchemy import db


class UserModel(db.Model):
    __tablename__='users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))
    def __init__(self, username, password):
        self.username=username
        self.password=password

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()
##        connection = sqlite3.connect('data.db')
##        cursor = connection.cursor()
##        query = "SELECT * FROM users WHERE username = ?"
##        result = cursor.execute(query, (username,))
##        print(result)
##        row = result.fetchone()
##        print(row)
##        if row is not None:
##            user = cls(row[0],row[1], row[2])
##        else:
##            user = None
##        connection.close()
##        return user

    @classmethod
    def find_by_userID(cls,_id):
        return cls.query.filter_by(id=_id).first()

##        connection = sqlite3.connect('data.db')
##        cursor = connection.cursor()
##        query = "SELECT * FROM users WHERE id = ?"
##        result = cursor.execute(query, (_id,))
##        row = result.fetchone()
##        if row is not None:
##            user = cls(row[0],row[1], row[2])
##        else:
##            user = None
##        connection.close()
##        return user

    def save_to_userdb(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_userdb(self):
        db.session.delete(self)
        db.session.commit()
