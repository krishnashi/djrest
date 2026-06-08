from fiveproj.models.items_model import ItemsModel
from fiveproj import db


class ItemController():
    @staticmethod
    def insert_data_controller(data):
        obj = ItemsModel(item_name = data['item_name'], quantity = data['quantity'])
        db.session.add(obj)
        db.session.commit()
        return {'id':obj.id, 'item_name': obj.item_name, 'quantity': obj.quantity}, 201

    @staticmethod
    def get_all_items():
        res = ItemsModel.query.all()
        print(res)
        items =  [{'id':obj.id, 'item_name': obj.item_name, 'quantity': obj.quantity} for obj in res]
        return {"items_list": items}

    @staticmethod
    def get_one_item(id):
        obj = ItemsModel.query.get(id)
        # print(res)
        if obj:
            # return {'id':obj.id, 'item_name':obj.item_name, 'quantity': obj.quantity}
            return obj
        return None

    @staticmethod
    def update_one_item(item_data):
        obj_data = ItemController.get_one_item(item_data['id'])
        if obj_data:
            obj_data.item_name = item_data['item_name']
            obj_data.quantity = item_data['quantity']
            db.session.add(obj_data)
            db.session.commit()
            return {'id':obj_data.id, 'item_name': obj_data.item_name, 'quantity': obj_data.quantity}
        return None


    @staticmethod
    def delete_one(id):
        obj_data = ItemController.get_one_item(id)
        if obj_data:
            db.session.delete(obj_data)
            db.session.commit()
            return {"msg": f"item with item id {id} deleted successfully"}
        return None

