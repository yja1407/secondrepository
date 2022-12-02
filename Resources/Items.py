from flask_restful import reqparse, Resource
from flask_jwt import jwt_required
##import sqlite3
from models.item import ItemModel

class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
        type=float,
        help="This field can't be blank"
    )
    parser.add_argument('store_id',
        type=int,
        required=True,
        help="every item needs a store_id"
    )


    @jwt_required()
    def get(self, name):
        item = ItemModel.finditem_by_name(name)
        if item is not None:
            return item.json()

        return {"message":"item was not found"},404


    def post(self,name):
#        if next(filter(lambda x: x['name'] == name, items), None):
#            return {'message': "an item was not found"},400
#        data = request.get_json()
        if ItemModel.finditem_by_name(name) is not None:
            return {'message': "an item exists"},400
        data = Item.parser.parse_args()
        item = ItemModel(name, data['price'],data['store_id'])
        try:
            item.save_to_db()
        except:
            return {"message":"an error occupied inserting the item"}, 500
        return item.json()



    def delete(self,name):
        item=Item.finditem_by_name(name)
        if item is not None:
            item.delete_from_db()
        return {'message':'Item deleted'}
#        global items
#        items= list(filter(lambda x: x['name'] != name, items))
#        return {'message':'item deleted'}
##        connection  = sqlite3.connect('data.db')
##        cursor = connection.cursor()
##        item_delete_query = "DELETE FROM itemlist WHERE name =?"
##        cursor.execute(item_delete_query, (name,))
##        connection.commit()
##        connection.close()

    def put(self,name):
        data = Item.parser.parse_args()
        item=ItemModel.finditem_by_name(name)
        if item is None:
            item = ItemModel(name, data['price'])
        else:
            item.price = data['price']
        item.save_to_db()
        return item.json()

##        updated_item = ItemModel(name, data['price'])
        #        item = next(filter(lambda x: x['name']==name,items), None)
##        if item is None:
##            try:
##                updated_item.insert()
##            except:
##                return {"message":"an error occuried inserting the item"}, 500
##        else:
##            try:
##                updated_item.update()
##            except:
##                return {"message":"an error occuried updating the item"}, 500
##        return updated_item.json()


class Itemlist(Resource):
    def get(self):
        return{'items':[item.json() for item in ItemModel.query.all()]}

##        connection  = sqlite3.connect('data.db')
##        cursor = connection.cursor()
##        select_item_query = "SELECT * FROM itemlist"
##        items = []
##        result = cursor.execute(select_item_query)
##        for row in result:
##            items.append({'id':row[0], 'name':row[1], 'price':row[2]})
##
##        connection.close()
##        return {'items': items}
