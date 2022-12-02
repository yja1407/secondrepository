from flask_restful import Resource
from models.store import StoreModel

class Store(Resource):
    def get(self,name):
        store =StoreModel.findstore_by_name(name)
        if store is not None:
            return store.json()
        else:
            return{'message':'Store not found'}, 404

    def post(self,name):
        if StoreModel.findstore_by_name(name):
            return {'message':'The store already exists'},400
        store = StoreModel(name)
        try:
            store.save_to_db()
        except:
            return {'message':'An error occuried while creating the stoore'},500
        return store.json(),201


    def delete(self,name):
        store =StoreModel.findstore_by_name(name)
        if store is not None:
            store.delete_from_db()
        return {'message':'Store deleted'}


class StoreList(Resource):
    def get(self):
        return{'stores':[store.json() for store in StoreModel.query.all()]}
