from os import name
from random import choices

from flask_restful import Resource, reqparse
from fiveproj.controllers.item_controller import ItemController
from flask_jwt_extended import jwt_required



class ItemsResource(Resource):
    def get(self):
        res = ItemController.get_all_items()
        return res, 200

    @jwt_required()
    def post(self):
        req_p = reqparse.RequestParser()
        req_p.add_argument(name="item_name", type=str, required=True)
        req_p.add_argument(name="quantity", type=int, required=True)
        data = req_p.parse_args()
        # print(data, type(data))
        res = ItemController.insert_data_controller(data)
        return res

class ItemsListResource(Resource):
    def get(self, id):
        res = ItemController.get_one_item(id)
        if res:
            return {'id':res.id, 'item_name':res.item_name, 'quantity': res.quantity}, 200
        return {"msg": f"for the given item id {id}, no item found"}, 404


    @jwt_required()
    def put(self, id):
        req_p = reqparse.RequestParser()
        req_p.add_argument(name="item_name", type=str, required=True)
        req_p.add_argument(name="quantity", type=int, required=True)
        item_data = req_p.parse_args()
        item_data['id'] = id
        res = ItemController.update_one_item(item_data)
        if res:
            return res
        return {"msg": f"for the given item id {id}, no item found"}, 404


    @jwt_required()
    def delete(self, id):
        res = ItemController.delete_one(id)
        if res:
            return res
        return {"msg": f"for the given item id {id}, no item found"}, 404




