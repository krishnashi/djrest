from flask_restful import Resource, reqparse
from fiveproj import db
from fiveproj.models.user_model import UserModel
from flask_jwt_extended import create_access_token


class LoginResource(Resource):
    def post(self):
        req_p = reqparse.RequestParser()
        req_p.add_argument(name="username", type=str, required=True)
        req_p.add_argument(name="password", type=str, required=True)
        data = req_p.parse_args()
        obj = UserModel.query.filter_by(username=data['username']).first()
        print(obj)
        if obj and obj.ch_pass_hash(data['password']):
            return {"access_token" : create_access_token(identity=data['username'])}
        return {"msg": "provide valid credentials"}

