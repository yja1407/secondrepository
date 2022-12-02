import sqlite3
from dbalchemy import db


class ItemModel(db.Model):
    __tablename__='itemlist'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    price = db.Column(db.Float(precision=2))

    store_id = db.Column(db.Integer, db.ForeignKey('Storelist.id'))
    store = db.relationship('StoreModel')

    def __init__(self, name, price, store_id):
        self.name = name
        self.price = price
        self.store_id = store_id

    def json(self):
        return {'name': self.name, 'price':self.price}

    @classmethod
    def finditem_by_name(cls, name):
        return cls.query.filter_by(name=name).first()
##        connection  = sqlite3.connect('data.db')
##        cursor = connection.cursor()
##        items_retrieve_query = "SELECT * FROM Itemlist WHERE name=?"
##        items_retrieve_result = cursor.execute(items_retrieve_query, (name,))
##        row = items_retrieve_result.fetchone()
##        connection.close()
        #print(row)

##        if row is not None:
##            return cls(row[0], row[1])
#            return {'item':{'name':row[0], 'price':row[1]}}

#        item = next(filter(lambda x: x['name'] == name, items), None)
#        print("HI from get method")
#        return {'item':item}, 200 if item else 404


    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
##        connection  = sqlite3.connect('data.db')
##        cursor = connection.cursor()
##        item_insert_query = "INSERT INTO itemlist VALUES (?,?)"
##        cursor.execute(item_insert_query, (self.name, self.price))
#               items.append(item)
##        connection.commit()
##        connection.close()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
##    def update(self):
##        connection  = sqlite3.connect('data.db')
##        cursor = connection.cursor()
##        update_item_query = "UPDATE itemlist SET price=? WHERE name=?"
##        cursor.execute(update_item_query, (self.price, self.name))
##        connection.commit()
##        connection.close()
