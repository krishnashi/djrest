from flask_restful import Resource, reqparse
from fiveproj.models.user_model import UserModel
from fiveproj import db


class RegisterResource(Resource):
    def post(self):
        req_p = reqparse.RequestParser()
        req_p.add_argument(name="username", type=str, required=True)
        req_p.add_argument(name="password", type=str, required=True)
        data = req_p.parse_args()
        obj = UserModel.query.filter_by(username=data['username']).first()
        if obj:
            return {"msg" : f"user with username {data['username']} already exists"}
        db_obj = UserModel(username=data['username'])
        db_obj.gen_pass_hash(data['password'])
        db.session.add(db_obj)
        db.session.commit()
        return {'msg': f"user with username {data['username']} registered successfully"}


