from models.user import UserModel
#from werkzeug.security import hmac
import hmac
from flask_jwt import jwt_required


#users = [
#User(1,'sasha', 'q')
#]

#username_mapping = {u.username: u for u in users}
#userID_mapping = {u.id: u for u in users}

def authenticate(username, password):
    #user = username_mapping.get(username, None)
    print("HI from authenticate")
    user = UserModel.find_by_username(username)
    if user is not None and hmac.compare_digest(user.password, password):
    #if user is not None and user.password == password:
        return user

def identity(payload):
    print("HI from identity")
    user_ID=payload['identity']
    #return userID_mapping.get(userID,None)
    return UserModel.find_by_userID(user_ID)


#users = [
#{
#'id':1
#'username': 'sasha'
#'password':q'
#}
#]

#username_mapping = {'sasha':
#{
#'id':1
#'username': 'sasha'
#'password':q'
#}
#}

#userID_mapping = {1:
#{
#'id':1
#'username': 'sasha'
#'password':q'
#}
