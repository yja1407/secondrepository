from flask import Flask
##, request
##from flask_restful import Resource
from flask_restful import Api
from flask_jwt import JWT
##,jwt_required
from sec import authenticate, identity
from Resources.user import UserRegister
from Resources.Items import Item, Itemlist
from Resources.store import Store, StoreList

app = Flask(__name__)
app.secret_key = 'jose' # app.config['JWT_SECRET_KEY']
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///C:/Flask_course/section6/data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
jwt = JWT(app,authenticate, identity)  # /auth

@app.before_first_request
def create_tables():
    db.create_all()


api.add_resource(Item,'/item/<string:name>')
api.add_resource(Itemlist,'/items')
api.add_resource(UserRegister,'/register')
api.add_resource(Store,'/store/<string:name>')
api.add_resource(StoreList,'/stores')

if __name__=='__main__':
    from dbalchemy import db
    db.init_app(app)
    app.run(port=4999)
